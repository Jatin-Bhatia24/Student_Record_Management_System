from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Student
from .forms import AddStudentForm


class Home(View):
    def get(self, request):
        search = request.GET.get('search', '')

        if search:
            stu_data = Student.objects.filter(
                name__icontains=search
            ) | Student.objects.filter(
                city__icontains=search
            )
        else:
            stu_data = Student.objects.all()

        total_students = Student.objects.count()

        return render(
            request,
            'core/home.html',
            {
                'studata': stu_data,
                'total_students': total_students,
                'search': search
            }
        )


class Add_Student(View):
    def get(self, request):
        fm = AddStudentForm()
        return render(
            request,
            'core/add-student.html',
            {'form': fm}
        )

    def post(self, request):
        fm = AddStudentForm(request.POST)

        if fm.is_valid():
            fm.save()
            return redirect('home')

        return render(
            request,
            'core/add-student.html',
            {'form': fm}
        )


class ViewStudent(View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)

        return render(
            request,
            'core/view-student.html',
            {'student': student}
        )


class Delete_Student(View):
    def post(self, request):
        id = request.POST.get('id')

        student = get_object_or_404(Student, id=id)
        student.delete()

        return redirect('home')


class EditStudent(View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        fm = AddStudentForm(instance=student)

        return render(
            request,
            'core/edit-student.html',
            {'form': fm}
        )

    def post(self, request, id):
        student = get_object_or_404(Student, id=id)

        fm = AddStudentForm(
            request.POST,
            instance=student
        )

        if fm.is_valid():
            fm.save()
            return redirect('home')

        return render(
            request,
            'core/edit-student.html',
            {'form': fm}
        )