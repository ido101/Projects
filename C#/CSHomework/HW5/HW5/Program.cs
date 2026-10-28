using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HW5
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Flower[] f1 = new Flower[3];
            f1[0] = new Flower(1,"rose", 10);
            f1[1] = new Flower(2, "sunflower", 15);
            f1[2] = new Flower(3, "lavender", 6);
            Flower[] f2 = new Flower[5];
            f2[0] = new Flower(1, "iris", 20);
            f2[1] = new Flower(2, "rose", 14);
            f2[2] = new Flower(3, "sunflower", 6);
            f2[3] = new Flower(4, "rose", 7);
            f2[4] = new Flower(5, "sunflower", 10);
            Bouquet b1 = new Bouquet("Bouqet 1", 3, f1);
            Bouquet b2 = new Bouquet("Bouqet 2", 5, f2);
            Compare(b1, b2);
            Console.WriteLine(b1.MoreExpensive(b2));
        }
        public static void Compare(Bouquet b1 ,Bouquet b2)
        {
            if (b1.MoreExpensive(b2))
            {
                Console.WriteLine(b1.GetQuantity());
                Console.WriteLine(b1.WorthInShekels());
            }
            else
            {
                Console.WriteLine(b2.GetQuantity());
                Console.WriteLine(b2.WorthInShekels());
            }
        }

    }
}
