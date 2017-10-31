#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import argparse, os
import mistune
import csv
from glob import glob
from pathlib import Path
from bs4 import BeautifulSoup

PURPOSE_STATEMENT_MIN = 300
FACT_RESULT_MIN = 1200
ANALOGS_MIN = 3
CRITERIAS_MIN = 3
ANALOG_REVIEW_MIN = 2000

def CheckRepo(repoPath):
    print('Checking for directory "' + repoPath + '"')
    directory = Path(repoPath)
    if directory.is_dir():
        print(' Directory'.ljust(26) +  '...\tExists!') # \u2713
        # Fix for checking any group dirs
        for subfolder in os.listdir(repoPath):
            # check for group dir
            if Path(os.path.join(repoPath, subfolder)).is_dir() and subfolder.isdigit():
                CheckGroupDirectory(os.path.join(repoPath, subfolder))
    else:
        print(" Directory doesn't exist!")

def CheckGroupDirectory(groupFolderPath):
    print('Checking for directory "' + groupFolderPath + '"')
    directory = Path(groupFolderPath)
    if directory.is_dir():
        print(' Directory'.ljust(26) +  '...\tExists!') # \u2713
        for subfolder in os.listdir(groupFolderPath):
            print(os.path.join(os.path.basename(groupFolderPath),subfolder))
            print('__')
            CheckNamedDirectory(os.path.join(groupFolderPath, subfolder))            
    else:
        print(" Directory doesn't exist!")

def CheckNamedDirectory(nameFolderPath):
    print('Checking for directory "' + nameFolderPath + '"')
    directory = Path(nameFolderPath)

    if directory.is_dir():
        print(' Directory'.ljust(26) +  '...\tExists!') # \u2713
        #CSV Name
        newCsvLine.append(os.path.basename(nameFolderPath))
        CheckForPaperBase(os.path.join(nameFolderPath, 'paper_base'))
        CheckForFactResult(nameFolderPath)
        CheckPurposeStatementFiles(nameFolderPath)
        CheckForAnalogs(nameFolderPath)
        #CSV Write Row
        csvWriter.writerow(newCsvLine)
        newCsvLine.clear()
    else:
        print(" Directory doesn't exist!")

def CheckForPaperBase(paperBaseFolderPath):
    #.pdf file(s)
    print("Checking /paper_base directory for .pdf files")
    if os.path.isdir(paperBaseFolderPath):
        print(' Directory'.ljust(26) +  '...\tExists!')
        pdfFiles = glob(os.path.join(paperBaseFolderPath,"*.{}".format('pdf')))
        if len(pdfFiles) != 0:
            #CSV Paper_base pdf
            newCsvLine.append('1')
            print(' .pdf files found:')
            for pdfFile in pdfFiles:
                print('  ' + os.path.basename(pdfFile))
        else:
            #CSV Paper_base pdf
            newCsvLine.append('0')
            print('  No .pdf files!')
    else:
        #CSV Paper_base pdf
        newCsvLine.append('0')
        print(" Directory doesn't exist!")

def CheckForFactResult(factResFolderPath):
    print("Checking for fact_result.md")
    if os.path.isfile(os.path.join(factResFolderPath,'fact_result.md')):
        print(' fact_result.md'.ljust(26) +  '...\tExists!')
        #CSV fact_result.md exists
        newCsvLine.append('1')
        factSymbolsNum = CountTextSymbols(os.path.join(factResFolderPath,"fact_result.md"))
        if factSymbolsNum >= FACT_RESULT_MIN:
            #CSV fact_result.md enough symbols
            newCsvLine.append('1')
            print("  Number of symbols in fact_result.md".ljust(50) + '...\tGood.')
        else:
            #CSV fact_result.md enough symbols
            newCsvLine.append('0')
            print("  Number of symbols in fact_result.md".ljust(50) + '...\tNot enough. Min = ' + \
                str(FACT_RESULT_MIN))
    else:
        #CSV fact_result.md doesn't exist
        newCsvLine.append('0')
        #CSV fact_result.md enough symbols
        newCsvLine.append('0')
        print(' fact_result.md'.ljust(26) +  '...\tdoes not exist!')

def CheckPurposeStatementFiles(nameFolderPath):
    print('Checking for purpose-statement files...')

    if (
        CheckForFile(nameFolderPath,"problem.md") &
        CheckForFile(nameFolderPath,"research_object.md") &
        CheckForFile(nameFolderPath,"research_subject.md") &
        CheckForFile(nameFolderPath,"goal.md") &
        CheckForFile(nameFolderPath,"tasks.md") &
        CheckForFile(nameFolderPath,"relevance.md") ):
        print(' All required files exist!\n  Counting symbols...')            
        purposeSymbNum = CountPurposeTextSymbols(nameFolderPath)
        if purposeSymbNum >= PURPOSE_STATEMENT_MIN:
            #CSV Purpose statements enough symbols
            newCsvLine.append('1')
            print("  Number of symbols in purpose statement's".ljust(50) + '...\tGood.')
        else:
            #CSV Purpose statements enough symbols
            newCsvLine.append('0')
            print("  Number of symbols in purpose statement's".ljust(50) + '...\tNot enough. Min = ' + \
                str(PURPOSE_STATEMENT_MIN))
    else:
        print(' Not all of required files exist!')
        #CSV Purpose statements enough symbols
        newCsvLine.append('0')

def CountPurposeTextSymbols(folderPath):
    allSymbolsNum = CountTextSymbols(os.path.join(folderPath, "problem.md")) + \
            CountTextSymbols(os.path.join(folderPath,"research_object.md")) + \
            CountTextSymbols(os.path.join(folderPath,"research_subject.md")) + \
            CountTextSymbols(os.path.join(folderPath,"goal.md")) + \
            CountTextSymbols(os.path.join(folderPath,"tasks.md")) + \
            CountTextSymbols(os.path.join(folderPath,"relevance.md"))
    if allSymbolsNum == 0:
        print('  All files are empty!')
    else:
        print('  All files'.ljust(26) + '...\t' + str(allSymbolsNum) + ' symbols')
    return allSymbolsNum

def CheckForAnalogs(analogsFolderPath):
    print("Checking for analogs.md")
    if os.path.isfile(os.path.join(analogsFolderPath,'analogs.md')):
        #CSV analogs.md exists
        newCsvLine.append('1')
        print(' analogs.md'.ljust(26) +  '...\tExists!')
        factSymbolsNum = CountTextSymbols(os.path.join(analogsFolderPath,"analogs.md"))
        if factSymbolsNum >= ANALOG_REVIEW_MIN:
            print("  Number of symbols in analogs.md".ljust(50) + '...\tGood.')
            #CSV analogs.md enough symbols
            newCsvLine.append('1')
        else:
            #CSV analogs.md enough symbols
            newCsvLine.append('0')
            print("  Number of symbols in analogs.md".ljust(50) + '...\tNot enough. Min = ' + \
                str(ANALOG_REVIEW_MIN))
        # .md parsing:
        soup = ParseMd(os.path.join(analogsFolderPath,'analogs.md'))
        titles = soup.find_all('h2')

        analogsH = 'none'
        criteriasH = 'none'
        sourcesH = 'none'

        for title in titles:
            if title.text.find("Сравнение аналогов") != -1:
                analogsH = title
            if title.text.find("Критерии сравнения аналогов") != -1:
                criteriasH = title
            if title.text.find("Источники") != -1:
                sourcesH = title
        
        if analogsH == 'none':
            print("  There is no Analogs title!")
            newCsvLine.append('0')
        else: # analogs check
            print("  Analogs title!".ljust(26) +  '...\tExists!')
            #find all h3 siblings
            analogChildren = []
            nextNode = analogsH
            while True:
                nextNode = nextNode.find_next_sibling()
                tag_name = ''
                try:
                    tag_name = nextNode.name
                except AttributeError:
                    tag_name = ""
                if tag_name == "h3":
                    analogChildren.append(nextNode)
                if tag_name == "h2" or nextNode.find_next_sibling() is None:
                    break

            if len(analogChildren) >= ANALOGS_MIN:
                print("   Number of analogs".ljust(25) + '...\tGood.')
                #CSV analogs num
                newCsvLine.append('1')
            else:
                print("   Number of analogs".ljust(25) + '...\tNot enough. Min = ' + \
                str(ANALOGS_MIN))
                #CSV analogs num
                newCsvLine.append('0')
        
        if criteriasH == 'none':
            print("  There is no Criterias title!")
            newCsvLine.append('0')
        else: #criterias check
            print("  Criterias title!".ljust(26) +  '...\tExists!')
            
            #find all h3 siblings
            criteriaChildren = []
            nextNode = criteriasH
            while True:
                nextNode = nextNode.find_next_sibling()
                tag_name = ''
                try:
                    tag_name = nextNode.name
                except AttributeError:
                    tag_name = ""
                if tag_name == "h3":
                    criteriaChildren.append(nextNode)
                if tag_name == "h2":
                    break
                        
            if len(criteriaChildren) >= CRITERIAS_MIN:
                print("   Number of analogs".ljust(25) + '...\tGood.')
                #CSV criterias num
                newCsvLine.append('1')
            else:
                print("   Number of analogs".ljust(25) + '...\tNot enough. Min = ' + \
                str(CRITERIAS_MIN))
                #CSV criterias num
                newCsvLine.append('0')
                

        if sourcesH == 'none':
            print("  There is no Sources title!")
            newCsvLine.append('0')
        else: #sources check
            print("  Sources title!".ljust(26) +  '...\tExists!')
            sourcesOl = sourcesH.find_next('ol')
            if sourcesOl is not None and  len( sourcesOl.findAll('li')) >= 1:
                print("   Number of sources".ljust(25) + '...\tAt least 1! Good!')
                #CSV sources num
                newCsvLine.append('1')
            else:
                print("   Number of sources".ljust(25) + '...\tNot enough. Min = 1')
                #CSV sources num
                newCsvLine.append('0')
    else:
        #CSV analogs.md exists
        newCsvLine.append('0')
        #CSV analogs.md enough symbols
        newCsvLine.append('0')
        #CSV analogs num
        newCsvLine.append('0')
        #CSV criterias num
        newCsvLine.append('0')
        #CSV sources num
        newCsvLine.append('0')
        print(' analogs.md'.ljust(26) +  '...\tdoes not exist!')

def CheckForFile(dirpath, filename):
    file = Path(dirpath+'/' + filename)
    
    if file.is_file():
        #CSV .md file exists
        newCsvLine.append('1')
        print('     ' + filename.ljust(25) + '...\tExists!')
        return True
    else:
        #CSV .md file doesn't exist
        newCsvLine.append('0')
        print('     ' + filename.ljust(25) + "...\tDoesn't exist!")
        return False

def ParseMd(file):
    f = open(file, 'r')
    try:
        mdText = f.read()
    except:
        mdText = " "
    htmlText = mistune.markdown(mdText)
    soup = BeautifulSoup(htmlText, 'html.parser')
    return soup

def CountTextSymbols(filename):
    soup = ParseMd(filename)
    pars = soup.find_all(['p','li'])
    allText = ""
    for t in pars:
        allText += t.text
    NONCOUNT_LETTERS = " ,.:;!?"
    symbolsNum = len([letter for letter in allText if letter not in NONCOUNT_LETTERS])
    if symbolsNum == 0:
        print('    ' + os.path.basename(filename).ljust(25) + '...\tEmpty!')
    else:
        print('    ' + os.path.basename(filename).ljust(25) + '...\t' + str(symbolsNum) + ' symbols')
    return symbolsNum

parser = argparse.ArgumentParser()
parser.add_argument('path', help='path to directory with .md files')
args = parser.parse_args()
repo_path = args.path

csvFile = open('result.csv', "w")
headers = ["Name", "Paper_base pdf", "fact_result.md exists", "fact_result.md enough symbols", \
        "problem.md exists", "research_object.md exists", "research_subject.md exists", \
        "goal.md exists", "tasks.md exists", "relevance.md exists", "Purpose statements enough symbols", \
        "analogs.md exists", "analogs.md enough symbols", "analogs num >= 3", "criteria num >= 3", "sources num >= 1"]

csvWriter = csv.writer(csvFile, delimiter=',')
csvWriter.writerows([headers])
newCsvLine = []
CheckRepo(repo_path)

csvFile.close()
csvFileRead = open('result.csv', "r")
csvReader = csv.reader(csvFileRead, delimiter=',')

csvResFile = open('sum_result.csv', "w")
res_headers = ["Name", "Выбор темы статьи и Фактический результат исследования (3)", \
        "Подготовка ответов на ключевые вопросы (7)", \
        "Сравнение аналогов или существующих подходов к решению проблемы (5)", \
        "Сумма оценок (15)"]
csvResWriter = csv.writer(csvResFile, delimiter=',')
csvResWriter.writerows([res_headers])
counter = 0
for row in csvReader:
    if counter == 0:
        counter = 1
        continue
    print(row)
    numlist = [int(x) for x in row[1:]]
    newCsvLine.append(row[0])
    newCsvLine.append(sum(numlist[0:3]))
    newCsvLine.append(sum(numlist[3:10]))
    newCsvLine.append(sum(numlist[10:]))
    newCsvLine.append(sum(numlist[0:]))
    csvResWriter.writerow(newCsvLine)
    newCsvLine.clear()

