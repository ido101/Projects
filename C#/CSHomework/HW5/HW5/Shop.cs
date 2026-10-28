using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HW5
{
    internal class Shop
    {
        private string name;
        private int quantity;
        private Product[] prods;
        
        public Shop(string name, int quantity)
        {
            this.name = name;
            this.quantity = quantity;
        }
        public Shop(string name, int quantity, Product[] prods)
        {
            this.name = name;
            this.quantity = quantity;
            this.prods = new Product[quantity];
            for (int i = 0; i < quantity; i++)
            {
                this.prods[i] = prods[i];
            }
        }
        public string GetName()
        {
            return name;
        }
        public int GetQuantity()
        {
            return quantity;
        }
        public Product[] GetProds()
        {
            return prods;
        }
        public void SetName(string name)
        {
            this.name = name;
        }
        public void SetQuantity(int quantity)
        {
            this.quantity = quantity;
        }
        public void SetProds(Product[] prods)
        {
            for (int i = 0; i < quantity; i++)
            {
                this.prods[i] = prods[i];
            }
        }
        public bool Enough(string prodName, int quan)
        {
            for (int i = 0; i < prods.Length; i++)
            {
                if(prodName == prods[i].GetName() && quan <= prods[i].GetQuantity())
                {
                    return true;
                }
            }
            return false;
        }
        public Product[] ProductsFromCategory(string category)
        {
            Product[] p = new Product[prods.Length];
            for (int i = 0; i < prods.Length; i++)
            {
                if (prods[i].GetCategory() == category)
                {
                    p[i] = new Product(prods[i].GetName(), prods[i].GetCategory(), prods[i].GetPrice(), prods[i].GetQuantity());
                }
            }
            return p;
        }
        public double Worth(string productName)
        {
            for (int i = 0; i < prods.Length; i++)
            {
                if (prods[i].GetName() == productName)
                {
                    return prods[i].GetQuantity() * prods[i].GetPrice();
                }
            }
            return 0;
        }
        public void HigherPrice(double p)
        {
            for (int i = 0; i < prods.Length; i++)
            {
                if (prods[i].GetPrice() > p)
                  Console.WriteLine(prods[i].GetName());
            }
        }
        public double WorthAllProducts()
        {
            double sum = 0;
            for (int i = 0; i < prods.Length; i++)
            {
                sum += prods[i].GetQuantity() * prods[i].GetPrice();
            }
            return sum;
        }
    }
}
