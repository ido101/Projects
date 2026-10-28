using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Targil2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int x = 8;
            int a = 5;
            x -= 1;
            int y = x;
            x = (2 * a - 5) * 2;
            a = (2 * a - 5) - x * 2;
            Console.WriteLine("X: " + x);
            Console.WriteLine("Y: " + y + ", A: " + a);
        }
    }
}
