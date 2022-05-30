#include "fizzBuzzTester.h"
#include <vector>
#include <string>
#include <iostream>

constexpr auto NUMBER_OF_RANDOM_TESTS = 10;
constexpr auto FIZZ_BUZZ_LENGTH = 10;

constexpr auto SUCCESS_MESSAGE = "Wszystko działa!\nGratulacje!";
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

std::vector<std::pair<int, std::string> > generateRandomAnswers(bool isCorrect)
{
    std::vector<std::pair<int, std::string> > randomAnswers;
    for(auto i = 0; i < FIZZ_BUZZ_LENGTH; i++)
    {
        int number = rand() % 1000 + 1;
        if(isCorrect)
        {
            randomAnswers.push_back({number, getAnswerFor(number)});
        }
        else
        {
            randomAnswers.push_back({number, getAnswerFor(number + 1)});
        }
    }

    // As answers are generated randomly, we need to ensure the there is an incorect example
    if(!isCorrect)
    {
        randomAnswers.push_back({5, "Fizz"});
    }

    return randomAnswers;
}

bool randomTest()
{
    bool isCorrect = rand() % 2 == 0; 
    auto dataForUser = generateRandomAnswers(isCorrect);

    try
    {
        bool userAnswer = testFizzBuzz(dataForUser);

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
