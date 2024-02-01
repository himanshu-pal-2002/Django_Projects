from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def equijoin(request):
    EMPO = Emp.objects.select_related('deptno').all()
    EMPO = Emp.objects.select_related('deptno').filter(ename='ALLEN')
    EMPO = Emp.objects.select_related('deptno').filter(sal__gt=2500)
    EMPO = Emp.objects.select_related('deptno').filter(mgr__ename='KING')
    EMPO = Emp.objects.select_related('deptno').filter(mgr__ename='JONES')
    EMPO = Emp.objects.select_related('deptno').filter(sal__lt=2500)
    EMPO = Emp.objects.select_related('deptno').filter(job='SALESMAN')
    EMPO = Emp.objects.select_related('deptno').filter(job='ANALYST')


    d={'EMPO':EMPO}
    return render(request,'showdata.html',d)


# create views for self joins:
def selfjoin(request):
    UO=Emp.objects.select_related('mgr').all()

    d={'UO':UO}

    return render(request,'selfjoin.html',d)

# create views for all three tables:
def combine(request):

    EMPOBJ=Emp.objects.select_related('deptno','mgr').all()
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(deptno_id=30)
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(ename='SMITH')
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(deptno__dloc='DALLAS')
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING')
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(mgr__sal__gt=2000)
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(deptno__dloc='DALLAS',mgr__sal__gt=2000)
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dloc='DALLAS') | Q(mgr__sal__gt=2000))
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(mgr=7839)
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(job='SALESMAN')
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH',mgr__ename='SCOTT')
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='RESEARCH') | Q(mgr__ename='SCOTT'))
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(sal__gt=2000)
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING',sal__gt=2500)
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(sal__gt=2000,mgr__sal__gt=2500)
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(deptno=10 , mgr__ename='SCOTT')
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(mgr__sal__lt=2500)
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='SALES')
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(deptno__deptno=20)
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(Q(deptno=10) | Q(mgr__ename='SCOTT'))
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(Q(sal__gt=2500) | Q(job='MANAGER'))
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(sal__gt=2500 , job='MANAGER')
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='SALES') | Q(mgr__ename='MARTIN'))
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING',deptno=20)
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(Q(mgr__ename='KING') | Q(deptno=20))
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dloc='CHICAGO') | Q(mgr__ename='SCOTT'))
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(deptno=10 , mgr__ename='SCOTT')
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dloc='DALLAS') | Q(mgr__sal__lt=2000))
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter( Q(mgr__ename='MARTIN') | Q(deptno__dname='SALES') )
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dloc='CHICAGO') | Q(mgr__ename='MARTIN'))
    EMPOBJ=Emp.objects.select_related('deptno','mgr').filter(Q(deptno=20) | Q(mgr__ename='SCOTT'))

    d={'EMPOBJ':EMPOBJ}

    return render(request,'combine.html',d)
