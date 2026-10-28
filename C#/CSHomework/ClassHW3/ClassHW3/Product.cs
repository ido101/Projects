using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassHW3
{
    internal class Product
    {
        private string productName;
        private string category;
        private double price;
        private int quantity;

        public Product(string productName, string category, double price, int quantity)
        {
            this.productName = productName;
            this.category = category;
            this.price = price;
            this.quantity = quantity;
        }

        public string GetProductName()
        {
            return productName;
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
        public void SetProductName(string productName)
        {
            this.productName = productName;
        }
        public void SetCategory(string category)
        {
            this.category = category;
        }
        public void SetPrice(double price)
        {
            this.price = price;
        }
        public void SetQuantity(int quantity)
        {
            this.quantity = quantity;
        }
    }
}
