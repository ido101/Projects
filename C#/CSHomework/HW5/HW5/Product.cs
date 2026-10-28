using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HW5
{
    internal class Product
    {
        private string name;
        private string category;
        private double price;
        private int quantity;

        public Product(string name, string category, double price, int quantity)
        {
            this.name = name;
            this.category = category;
            this.price = price;
            this.quantity = quantity;
        }
        public string GetName()
        {
            return name;
        }
        public string GetCategory()
        {
            return category;
        }
        public double GetPrice()
        {
            return price;
        }
        public int GetQuantity()
        {
            return quantity;
        }
        public void SetPrice(double price)
        {
            this.price = price;
        }
        public void SetQuantity(int quantity)
        {
            this.quantity = quantity;
        }
        public void SetCategory(string category)
        {
            this.category = category;
        }
        public void SetName(string name)
        {
            this.name = name;
        }
    }
}
