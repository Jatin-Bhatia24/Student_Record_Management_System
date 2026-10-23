from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Student
from .forms import AddStudentForm


def get_students(search):
    """Latest students first, optionally filtered by name or city."""
    students = Student.objects.all().order_by('-date_added')
    if search:
        students = students.filter(
            Q(name__icontains=search) | Q(city__icontains=search)
        )
    return students


class Home(View):
    PREVIEW_COUNT = 3

    def get(self, request):
        search = request.GET.get('search', '').strip()
        students = get_students(search)
        matched = students.count()

        return render(request, 'core/home.html', {
            'studata': students[:self.PREVIEW_COUNT],
            'total_students': Student.objects.count(),
            'has_more': matched > self.PREVIEW_COUNT,
            'search': search,
        })


class AllStudents(View):
    PER_PAGE = 10

    def get(self, request):
        search = request.GET.get('search', '').strip()
        paginator = Paginator(get_students(search), self.PER_PAGE)
        page_obj = paginator.get_page(request.GET.get('page'))

        return render(request, 'core/all-students.html', {
            'page_obj': page_obj,
            'search': search,
        })


class Add_Student(View):
    def get(self, request):
        return render(request, 'core/add-student.html', {'form': AddStudentForm()})

    def post(self, request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('home')
        return render(request, 'core/add-student.html', {'form': fm})


class ViewStudent(View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        return render(request, 'core/view-student.html', {'student': student})


class Delete_Student(View):
    def post(self, request):
        student = get_object_or_404(Student, id=request.POST.get('id'))
        student.delete()
        return redirect('home')


class EditStudent(View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        return render(request, 'core/edit-student.html', {'form': AddStudentForm(instance=student)})

    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        fm = AddStudentForm(request.POST, instance=student)
        if fm.is_valid():
            fm.save()
            return redirect('home')
        return render(request, 'core/edit-student.html', {'form': fm})