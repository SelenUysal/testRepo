using System;

namespace ComplexityExample
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a value (number or string): ");
            var input = Console.ReadLine();
            string result = CheckInput(input);
            Console.WriteLine(result);
        }

        static string CheckInput(string value)
        {
            if (value == null)
            {
                return "Input is null";
            }
            else if (value.Equals("undefined", StringComparison.OrdinalIgnoreCase))
            {
                return "Input is undefined";
            }
            else if (value.Length == 0)
            {
                return "Input is an empty string";
            }
            else if (int.TryParse(value, out int number))
            {
                if (number < 0)
                {
                    return "Input is a negative number";
                }
                else if (number == 0)
                {
                    return "Input is zero";
                }
                else if (number > 100)
                {
                    return "Input is greater than 100";
                }
                else
                {
                    return "Input is a valid number between 1 and 100";
                }
            }
            else if (value.StartsWith("Hello"))
            {
                return "Input starts with Hello";
            }
            else if (value.Length < 5)
            {
                return "Input string is too short";
            }
            else if (value.Length > 20)
            {
                return "Input string is too long";
            }
            else
            {
                switch (value.ToLower())
                {
                    case "apple":
                        return "Input is an apple";
                    case "banana":
                        return "Input is a banana";
                    case "orange":
                        return "Input is an orange";
                    default:
                        return "Input is a valid string but not a fruit";
                }
            }
        }
    }
}
