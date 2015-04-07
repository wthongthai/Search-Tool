from django.http import HttpResponse
from django.shortcuts import render
from search.models import Textbooks, Questions
from forms import SearchForm
from django.core.exceptions import ObjectDoesNotExist
from webtoolspy import view_query

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # gather user input
            book_code = request.POST['book_code']
            chapter = request.POST['chapter']
            mode = request.POST['mode']
            question_name = request.POST['question_name']
            question_name_exclude = request.POST['question_name_exclude']
            question_field = request.POST['question_field']
            #question_field_exclude= request.POST['question_field_exclude']
            answer_bool = request.POST.get('answer_bool', False)
            answer_field = request.POST['answer_field']
            solution_bool = request.POST.get('solution_bool', False)
            solution_field = request.POST['solution_field']
            #testing = request.POST['testing']
            # process book codes
            book_code = book_code.replace(" ","")
            book_code_list = book_code.split(",")
            book_obj_list = []
            # validate book codes
            for b in book_code_list:
                try:
                    book_obj = Textbooks.objects.get(code=b)
                    book_obj_list.append(book_obj)
                except Textbooks.DoesNotExist:
                    return HttpResponse('Invalid book code')
            # construct query
            questions = view_query.query(book_obj_list, chapter, mode, question_name, question_name_exclude, question_field, answer_bool, answer_field, solution_bool, solution_field)
            questions_eval = eval(questions)
            question = [q.code for q in questions_eval]
            count = len(question)
            return render(request, 'question_list.html',{'count': count, 'book': book_code, 'question': question, 'query_string': questions})
    else:
        form = SearchForm()
    return render(request, 'search_form.html', {'form': form})
