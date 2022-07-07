#include "fizzBuzzTester.h"
#include <string>
#include <iostream>

constexpr auto NUMBER_OF_RANDOM_TESTS = 10;
constexpr auto MIN_FIZZ_BUZZ_LENGTH = 5;
constexpr auto MAX_FIZZ_BUZZ_LENGTH = 25;

constexpr auto SUCCESS_MESSAGE = "Działa!\nCiekawe jak idzie HaPekowi...";
constexpr auto FAIL_MESSAGE = "Coś chyba nie działa...\nPopraw program i spróbuj ponownie";

std::string getAnswerFor(int number)
{
    std::string expected = "";

    if(number % 3 == 0)
    {
        expected += "Fizz";
    }
    if(number % 5 == 0)
    {
        expected += "Buzz";
    }
    if(expected == "")
    {
        expected = std::to_string(number);
    }

    return expected;
}

void generateQuestions(int questions[], int len)
{
    for(auto i = 0; i < len; i++)
    {
        // Generate number in range <1, 100>
        questions[i] = rand() % 100 + 1;
    }
}

void generateAnswers(std::string answers[], int questions[], int len)
{
    for(auto i = 0; i < len; i++)
    {
        answers[i] = getAnswerFor(questions[i]);
    }
}

void makeAnswersIncorrect(std::string answers[], int questions[], int len)
{
    auto randIndex = rand() % len;
    // Answer for (question+1) is never the same as answer for (question)
    answers[randIndex] = getAnswerFor(questions[randIndex] + 1);
}

bool randomTest()
{
    bool isCorrect = rand() % 2 == 0; 
    auto numberOfQuestions = rand() % (MAX_FIZZ_BUZZ_LENGTH - MIN_FIZZ_BUZZ_LENGTH + 1) + MIN_FIZZ_BUZZ_LENGTH;
    int questions[numberOfQuestions];
    std::string answers[numberOfQuestions];

    generateQuestions(questions, numberOfQuestions);
    generateAnswers(answers, questions, numberOfQuestions);

    if(!isCorrect)
    {
        makeAnswersIncorrect(answers, questions, numberOfQuestions);
    }

    try
    {
        bool userAnswer = testFizzBuzz(questions, answers, numberOfQuestions);

        return isCorrect == userAnswer;
    }
    catch(const std::exception& e)
    {
        return false;
    }
}

bool test()
{
    auto komunikat = "";

    for(auto i = 0; i < NUMBER_OF_RANDOM_TESTS; ++i)
    {
        if(!randomTest())
        {
            komunikat = FAIL_MESSAGE;
            return false;
        }
    }

    komunikat = SUCCESS_MESSAGE;
    return true;
}

int main()
{
    test();  
}