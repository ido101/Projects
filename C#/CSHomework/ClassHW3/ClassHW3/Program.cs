using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassHW3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Product[] shop = new Product[500];
            for (int i = 0; i < 500; i++)
            {
                shop[i] = MakeProduct();
            }
            Console.WriteLine(AllWorth(shop));
        }
        public static Product MakeProduct()
        {
            string n = Console.ReadLine();
            string c = Console.ReadLine();
            double pr = double.Parse(Console.ReadLine());
            int q = int.Parse(Console.ReadLine());
            Product p = new Product(n, c, pr, q);
            return p;
        }
        public static void isEnough(Product[] shop, string pName, int amount)
        {
            for (int i = 0; i < shop.Length; i++)
            {
                if (shop[i].GetProductName() == pName)
                {
                    if (amount > shop[i].GetQuantity())
                        Console.WriteLine("Enough");
                    else
                        Console.WriteLine("Not Enough");
                }
            }
        }
        public static int ProductsFromCategory(Product[] shop, string categoryName)
        {
            int count = 0;
            for (int i = 0; i < shop.Length; i++)
            {
                if (shop[i].GetCategory() == categoryName)
                    count++;
            }
            return count;
        }
        public static double Worth(Product[] shop, string name)
        {
            double worth = 0;
            for (int i = 0; i < shop.Length; i++)
            {
                if (shop[i].GetProductName() == name)
                {
                    worth = shop[i].GetQuantity() * shop[i].GetPrice();
                }
            }
            return worth;
        }
        public static Product[] Update(Product[] shop)
        {
            for (int i = 0; i < shop.Length; i++)
            {
                shop[i].SetPrice(shop[i].GetPrice() * 1.1);
            }
            return shop;
        }
        public static void BiggerThanPrice(Product[] shop, double p)
        {
            for (int i = 0; i < shop.Length; i++)
            {
                if (shop[i].GetPrice() > p)
                {
                    Console.WriteLine(shop[i].GetProductName());
                }
            }
        }
        public static double AllWorth(Product[] shop)
        {
            double sum = 0;
            for (int i = 0; i < shop.Length; i++)
            {
                sum += shop[i].GetPrice() * shop[i].GetQuantity();
            }
            return sum;
        }
    }
}
