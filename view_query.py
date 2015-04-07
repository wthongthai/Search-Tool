from search.models import Textbooks, Questions
from django.db.models import Q
import re

# function to construct query string based on user input, Q object is used to construct "AND" and "OR" relationships
def query(book_obj_list, chapter, mode, question_name, question_name_exclude, question_field, answer_bool, answer_field, solution_bool, solution_field):
    query_string = ''
    num_book = len(book_obj_list)
    if num_book > 0:
        query_string += 'Questions.objects.filter(('
        for n in range(len(book_obj_list)):
            book_id = str(book_obj_list[n].id)
            if n == 0:
                query_string += 'Q(textbook='+book_id+')'
            else:
                query_string += '|Q(textbook='+book_id+')'
    query_string += ')'
    if chapter:
        query_string += '&Q(chapter=chapter)'
    if question_field or answer_field or solution_field:
        query_string += '&('
        if question_field:
            query_string += '(' + field_parser(question_field, 'question') + ')'
        if answer_field:
            query_string += bool_check(question_field, answer_bool)
            #query_string += 'Q(answer__icontains=answer_field)'
            query_string += '(' + field_parser(answer_field, 'answer') + ')'
        if solution_field:
            query_string += bool_check_2(question_field, answer_field, solution_bool)
            #query_string += 'Q(solution__icontains=solution_field)'
            query_string += '(' + field_parser(solution_field, 'solution') + ')'
        query_string += ')'
    if question_name:
        query_string += '&(' + field_parser(question_name, 'code') + ')'
        #query_string += '&Q(code__icontains=question_name)'
    if mode:
        query_string += '&Q(mode__icontains=mode)'
    if question_name_exclude:
        query_string += ')'
        if question_name_exclude:
            query_string += '.exclude(code__icontains=question_name_exclude)'
    else:
        query_string += ')'
    query_string += '.order_by("code")'
    return query_string

# fuction to parse userinput to support AND, OR, AND-NOT, OR-NOT in the question, answer, and solution field
def field_parser(usr_input, field):
    string = str(usr_input)
    enter_field = field+'__icontains'
    if ('{AND}' in string) or ('{OR}' in string) or ('{ANOT}' in string) or ('{ONOT}' in string):
        output_int1 = re.sub(r'{AND}', '{!AND!}', string)
        output_int2 = re.sub(r'{OR}', '{!OR!}', output_int1)
        output_int3 = re.sub(r'{ANOT}', '{!ANOT!}', output_int2)
        output_int4 = re.sub(r'{ONOT}', '{!ONOT!}', output_int3)
        output_int5 = re.sub(r'(^.*$)', '!}\\1{!', output_int4)
        output_int6 = re.sub(r'(!\})(.*?)(\{!)', '\\1Q(field__icontains="\\2")\\3', output_int5)
        output_int7 = re.sub(r'\{!AND!\}', '&', output_int6)
        output_int8 = re.sub(r'\{!OR!\}', '|', output_int7)
        output_int9 = re.sub(r'\{!ANOT!\}', '&~', output_int8)
        output_int10 = re.sub(r'\{!ONOT!\}', '|~', output_int9)
        output_int11 = re.sub(r'^!}', '', output_int10)
        output_int12 = re.sub(r'{!$', '', output_int11)
        output = re.sub(r'field__icontains', enter_field, output_int12)
        return output
    else:
        return 'Q('+field+'__icontains="'+string+'")'

def bool_check(prev_field, bool_select):
    if prev_field:
        if bool_select:
            return '|'
        else:
            return '&'
    else:
        return ''

def bool_check_2(prev_field_1, prev_field_2, bool_select):
    if prev_field_1 or prev_field_2:
        if bool_select:
            return '|'
        else:
            return '&'
    else:
        return ''
