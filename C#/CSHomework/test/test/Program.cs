using System;

namespace test
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int[] a = { 1, 4, 5, 3, 8, 6 };
            Console.WriteLine(Biggest(a));
        }
        public static int Biggest(int[] arr)
        {
            int b = 0;
            for (int i = 1; i < arr.Length; i++)
            {
                if (arr[i] > arr[b])
                    b = i;
            }
            return b;
        }
    }
}
