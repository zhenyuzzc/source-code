#ifndef STUDENT_H
#define STUDENT_H
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
//也作为学号输入是否正确的判断条件
#define N 6 //方便以后修改班级人数,

//定义单个学生的结构体
//此时内存没有给空间
typedef struct student{
    char name[16];
    int age;
    int id;
    int scoe;
}STU;

//定义这班级所有学生的结构体
//此时内存没有给空间

typedef struct Class{
    STU mum[N];
    int count;
}CLASS;

void Menu(); //打印菜单函数
void ADD(CLASS *P); //查看所有学生的函数
void SEE(CLASS *P); //查看需所有学生信息的函数
void MOD(CLASS *P); //根据学号修改学生信息的函数
void DEL(CLASS *P); //根据学号删除学生信息的函数
void SORT(CLASS *P); //根据成绩将学生降序排序的函数

#endif