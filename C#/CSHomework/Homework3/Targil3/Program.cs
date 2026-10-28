using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Targil3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int b = 3;
            int a = 2;
            b -= 3;
            int y = b;
            a = (3 * a + 1) * 2;
            b = (2 * b - 2) - a;
            Console.WriteLine(b);
            Console.WriteLine(y + " " + a);
        }
    }
}
