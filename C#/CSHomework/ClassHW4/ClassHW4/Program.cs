using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassHW4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Baby b1 = new Baby("baby1");
            Baby b2 = new Baby("baby2");
            Console.WriteLine(MonthsUnderAvg(b1));
            Console.WriteLine(MonthsUnderAvg(b2));
        }
        public static string HigherAverage(Baby b1, Baby b2)
        {
            double avg1 = 0;
            double avg2 = 0;
            for (int i = 0; i < 12; i++)
            {
                avg1 += b1.GetHeight()[i];
                avg2 += b2.GetHeight()[i];
            }
            avg1/= 12;
            avg2/= 12;
            if(avg1 > avg2)
            {
                return b1.GetName();
            }
            return b2.GetName();
        }
        public static int MonthsUnderAvg(Baby b1)
        {
            int count = 0;
            for (int i = 0; i < 12; i++)
            {
                if (b1.GetWeight()[i] < b1.WeightAvg())
                    count++;
            }
            return count;
        }
    }
}
