using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HW5
{
    internal class Bouquet
    {
        private string name;
        private int quantity;
        private Flower[] flowers;
        public Bouquet(string name, int quantity)
        {
            this.name = name;
            this.quantity = quantity;
        }
        public Bouquet(string name, int quantity, Flower[] flowers)
        {
            this.name = name;
            this.quantity = quantity;
            this.flowers = new Flower[quantity];
            for (int i = 0; i < quantity; i++)
            {
                this.flowers[i] = flowers[i];
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
        public Flower[] GetFlowers()
        {
            return flowers;
        }
        public void SetName(string name)
        {
            this.name = name;
        }
        public void SetQuantity(int quantity)
        {
            this.quantity = quantity;
        }
        public void SetFlowers(Flower[] flowers)
        {
            for (int i = 0; i < flowers.Length; i++)
            {
                flowers[i] = null;
            }
            for (int i = 0; i < quantity; i++)
            {
                this.flowers[i] = flowers[i];
            }
        }
        public double WorthInShekels()
        {
            Console.WriteLine("Enter dollar rate");
            double rate = double.Parse(Console.ReadLine());
            double sum = 0;
            for (int i = 0; i < quantity; i++)
            {
                sum += flowers[i].getPrice();
            }
            sum *= 0.9 * rate;
            return sum;
        }
        public int HowManyTypes()
        {
            int count = 0;
            string[] TypesMentioned = new string[quantity];
            bool exists = false;
            for (int i = 0; i < quantity; i++)
            {
                for (int j = 0; j < quantity; j++)
                {
                    if (flowers[i].getType() == TypesMentioned[j])
                    {
                        exists = true;
                    }
                }
                if(!exists)
                {
                    count++;
                    TypesMentioned[i] = flowers[i].getType();
                }
                exists = false;
            }
            return count;
        }
        public int AmountThatTypeFound(string type)
        {
            int count = 0;
            for (int i = 0; i < quantity; i++)
            {
                if (flowers[i].getType() == type)
                    count++;
            }
            return count;
        }
        public double Cheapest()
        {
            double cheapest = flowers[0].getPrice();
            for (int i = 1; i < quantity; i++)
            {
                if(cheapest > flowers[i].getPrice())
                {
                    cheapest= flowers[i].getPrice();
                }
            }
            return cheapest;
        }
        public bool MoreExpensive(Bouquet b)
        {
            if(b.WorthInShekels() > this.WorthInShekels())
                return true;
            return false;
        }

    }
}
