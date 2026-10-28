using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassHW4
{
    internal class Baby
    {
        private string name;
        private double[] h;
        private double[] w;

        public Baby(string name)
        {
            h = new double[12];
            w = new double[12];
            this.name = name;
            for (int i = 0; i < 12; i++)
            {
                h[i] = 0;
                w[i] = 0;
            }
          
        }
        public string GetName()
        {
            return name;
        }
        public double[] GetHeight()
        {
            return h;
        }
        public double[] GetWeight()
        {
            return w;
        }
        public void SetName(string name)
        {
            this.name = name;
        }
        public void SetHeight(double[] h)
        {
            this.h = h;
        }
        public void SetWeight(double[] w)
        {
            this.w = w;
        }
        public override string ToString()
        {
            string hToString = "" + h[0];
            string wToString = "" + w[0];
            for (int i = 1; i < 12; i++)
            {
                hToString += ", " + h[i];
                wToString += ", " + w[i];
            }
            return name + ", [" + hToString + "]" + ", [" + wToString + "]";
        }
        public void SetMeasurement(int month, double height, double weight)
        {
            h[month-1] = height;
            w[month-1] = weight;
        }
        public double HeightAvg()
        {
            double avg = 0;
            int count = 0;
            for (int i = 0; i < 12; i++)
            {
                if (h[i] != 0)
                    avg += h[i];
                    count++;
            }
            return avg/count;
        }
        public double WeightAvg()
        {
            double avg = 0;
            int count = 0;
            for (int i = 0; i < 12; i++)
            {
                if (w[i] != 0)
                    avg += w[i];
                    count++;
            }
            return avg / count;
        }
        public double LastBMI()
        {
            int last = 0;
            for (int i = 0; i < 12; i++)
            {
                if (h[i] != 0)
                    last = i;
            }
            return w[last] / (h[last] * h[last]);
        }
        public int CountMeasurements()
        {
            int count = 0;
            for (int i = 0; i < 12; i++)
            {
                if (h[i] != 0)
                {
                    count++;
                }
            }
            return count;
        }
        public void PrintHeightMeasurements()
        {
            string hToString = "" + h[0];
            for (int i = 1; i < 12; i++)
            {
                hToString += ", " + h[i];
            }
            Console.WriteLine("[" + hToString + "]");
        }
        public void PrintWeightMeasurements()
        {
            string wToString = "" + h[0];
            for (int i = 1; i < 12; i++)
            {
                wToString += ", " + w[i];
            }
            Console.WriteLine("[" + wToString + "]");
        }
        public void PrintWhenWeightLost()
        {
            for (int i = 1; i < 12; i++)
            {
                if (w[i] < w[i - 1])
                {
                    Console.WriteLine("Weight lost between months " + (i-1) + "and " + i);
                }
            }
        }
    }
}
