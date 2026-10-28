using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Targil5
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int perHour;
            Console.WriteLine("Enter your rank:");
            int r = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter amount of hours you worked this month:");
            int hrs = int.Parse(Console.ReadLine());
            switch (r)
            {
                case 1:
                    perHour = 100;
                    break;
                case 2:
                    perHour = 80;
                    break;
                case 3:
                    perHour = 50;
                    break;
                default:
                    perHour = 20; 
                    break;
            }
            int salary = perHour * hrs;
            Console.WriteLine("Your salary is: " + salary);
        }
    }
}
