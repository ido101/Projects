using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Targil4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the height and width:");
            int hgt = int.Parse(Console.ReadLine());
            int wdt = int.Parse(Console.ReadLine());
            int area = hgt * wdt;
            int perimeter = 2 * (hgt + wdt);
            Console.WriteLine("perimeter: " + perimeter);
            Console.WriteLine("area: " + area);
            if (hgt == wdt)
            {
                Console.WriteLine("square");
            }
            else {
                Console.WriteLine("not square"); 
                Console.WriteLine(Math.Abs(hgt - wdt));
            }
        }
    }
}
