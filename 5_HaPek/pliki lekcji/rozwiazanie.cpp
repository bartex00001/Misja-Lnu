#include <vector>
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

bool testFizzBuzz(std::vector<std::pair<int, std::string> >& userAnswers)
{
    for(auto ans: userAnswers)
    {
        if(!checkAnswer(ans.first, ans.second))
        {
            return false;
        }
    }

    return true;
}
