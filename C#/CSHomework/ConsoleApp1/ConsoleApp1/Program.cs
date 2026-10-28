using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] election = new int[9];
            for (int i = 0; i < election.Length; i++)
            {
                election[i] = 0;
            }
            Console.WriteLine("Enter Choice:");
            int choice = int.Parse(Console.ReadLine());
            while (choice != 999)
            {
                election[choice]++;
                Console.WriteLine("Enter Choice:");
                choice = int.Parse(Console.ReadLine());
            }
            int max = 1;
            for (int i = 1; i < election.Length; i++)
            {
                if (election[i] > election[max])
                    max = i;
                Console.WriteLine(i + "-" + election[i]);
            }
            Console.WriteLine(max);
        }
    }
}
