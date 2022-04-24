"""
This is a really simple and basic script to allow me to pick what to revise and when
CSV will store the basic data about each chapter mixed exercise
A 2nd CSV will store whats already been done
The code will then be able to spit out:
 - Todays revision
 - % of chapter completed
 - % of book
 - % of all


why why why why teh fuck am i writing this instead of just actaully revising like whtat the fuck ive spent an hour writi
ng some shitty shitty code just to procarastinate from doing maths
"""

import csv
import time, random

def todaysPlan():
    """uhhhhhhhhhhhhhh"""

    qs = {'1':[],'2':[],'3':[],'4':[]}




    for book in qs.keys():
        with open('1.csv') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')

            for row in reader:
                if str(row['Book']) == str(book):
                    for i in range(1, int(row['Qs'])+1):
                        found = False
                        with open('2.csv') as csvfile1:
                            reader1 = csv.DictReader(csvfile1, delimiter=',')
                            for row1 in reader1:
                                if (str(row1['Book']) == str(book) and str(row1['Chapter']) == str(row['Chapter']) and row1['Question']==str(i)):
                                    found=True
                            if not found:
                                qs[book].append([row['Chapter'], i])


    x = random.sample(qs['1'], 4)
    print('From Book 1 do:')
    for i in x:
        print(i)

    x = random.sample(qs['2'], 4)
    print('From Book 2 do:')
    for i in x:
        print(i)

    x = random.sample(qs['3'], 3)
    print('From Book 3 do:')
    for i in x:
        print(i)

    x = random.sample(qs['4'], 1)
    print('From Book 4 do:')
    for i in x:
        print(i)

    print()

def addQs():
    book, chapter, q = input('Enter book,chapter,q - ').split(',')
    correct = input('Correct? ')
    with open('2.csv', 'a', newline='') as csvfile:
        fieldnames = ['Book', 'Question', 'Chapter', 'Correct', 'Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'Book': book, 'Chapter': chapter, 'Correct': correct, 'Date':str(int(time.time())) })

def allPer():
    correct, attempt, total = 0, 0, 0

    with open('1.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            total += int(row['Qs'])

    with open('2.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if str(row['Chapter']) == '1':
                correct += 1
                attempt += 1
            else:
                attempt += 1

def bookPer():
    book = input('Enter Book Num - ')
    correct, attempt,total = 0, 0,0

    with open('1.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if str(row['Book']) == str(book):
                total += int(row['Qs'])

    with open('2.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if str(row['Book']) == str(book):
                if str(row['Chapter']) == '1':
                    correct += 1
                    attempt += 1
                else:
                    attempt += 1

    print(f"Total Questions     - {total}")
    print(f"Total correct       - {correct}")
    print(f"Total attempts      - {attempt}")

    print('\n\n')
    print(f"Percentage Correct  - {(correct / total) * 100}")
    print(f"Percentage Attempt  - {(attempt / total) * 100}")

def chapterPer():
    book = input('Enter Book Num - ')
    chapter = input('Enter Chapter Num - ')
    correct, attempt = 0,0
    with open('1.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if str(row['Book'])==str(book) and str(row['Chapter'])==str(chapter):
                total = int(row['Qs'])
    with open('2.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if str(row['Book'])==str(book) and str(row['Chapter'])==str(chapter):
                if str(row['Chapter'])=='1':
                    correct += 1
                    attempt += 1
                else:
                    attempt += 1

    print(f"Total Questions     - {total}")
    print(f"Total correct       - {correct}")
    print(f"Total attempts      - {attempt}")

    print('\n\n')
    print(f"Percentage Correct  - {(correct/total) *100}")
    print(f"Percentage Attempt  - {(attempt / total) * 100}")


while True:
    print('Select a function')
    print('1 - Todays plan')
    print('2 - % of chapter completed')
    print('3 - % of book completed')
    print('4 - % of all')
    print('5 - Add questions completed')
    x = input('> ')
    if x == '1':
        todaysPlan()
    elif x == '2':
        chapterPer()
    elif x == '3':
        bookPer()
    elif x == '4':
        allPer()
    elif x =='5':
        addQs()
    else:
        print('invalid')
