using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HW5
{
    internal class Flower
    {
        private int number;
        private string type;
        private double price;
        public Flower(int number, string type, double price)
        {
            this.number = number;
            this.type = type;
            this.price = price;
        }   
        public int getNumber() { return number; }
        public string getType() { return type; }
        public double getPrice() { return price; }
        public void SetNumber(int number) { this.number = number;}
        public void SetType(string type) { this.type = type;}
        public void SetPrice(double price) { this.price = price;}

    }
}
