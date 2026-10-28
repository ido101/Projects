using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WorkForQuiz
{
    internal class Beged
    {
        private string type;
        private string color;
        private double price;
        public Beged(string type, string color, double price)
        {
            this.type = type;
            this.color = color;
            this.price = price;
        }
        public double GetPrice()
        {
            return price;
        }
        public string GetType()
        {
            return type;
        }
        public string GetColor()
        {
            return color;
        }
    }
}
