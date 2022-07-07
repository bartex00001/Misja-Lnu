#include <string>

bool checkAnswer(int number, std::string answer)
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

    return answer == expected;
}

bool testFizzBuzz(int questions[], std::string answers[], int len)
{
    for(int i = 0; i < len; i++)
    {
        if(!checkAnswer(questions[i], answers[i]))
        {
            return false;
        }
    }

    return true;
}
