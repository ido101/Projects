using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Unit4.CollectionsLib;

namespace HW6
{
    internal class Program
    {
        public static Node<bool> MakeCandles()
        {
            Node<bool> tmp8 = new Node<bool>(false);
            Node<bool> tmp7 = new Node<bool>(false, tmp8);
            Node<bool> tmp6 = new Node<bool>(false, tmp7);
            Node<bool> tmp5 = new Node<bool>(false, tmp6);
            Node<bool> tmp4 = new Node<bool>(false, tmp5);
            Node<bool> tmp3 = new Node<bool>(false, tmp4);
            Node<bool> tmp2 = new Node<bool>(false,tmp3);
            Node<bool> tmp = new Node<bool>(false, tmp2);
            return tmp;
        }
        public static Node<bool> Shamash(Node<bool> n1, Node<bool> shamash, int index)
        {
            Node<bool> tmp = n1;
            if(index== 0)
            {
                shamash.SetNext(n1);
                return shamash;
            }
            for (int i = 0; i < index-1; i++)
            {
                tmp = tmp.GetNext();
            }
            shamash.SetNext(tmp.GetNext());
            tmp.SetNext(shamash);
            return n1;
        }
        public static Node<bool> LightUp(Node<bool> n1, int day)
        {
            Node<bool> tmp = n1;
            for (int i = 0; i < day; i++)
            {
                tmp.SetInfo(true);
                tmp = tmp.GetNext();
            }
            for (int i = day; i < 8; i++)
            {
                tmp = tmp.GetNext();
            }
            tmp.SetInfo(true);
            return n1;
        }

        public static Node<int> Sevivon(Node<int> n1, char tav)
        {
            Node<int> tmp = n1;
            if (tav == 'נ')
            {
                while (tmp.GetNext() != null)
                {
                    tmp = tmp.GetNext();
                }
                Console.WriteLine("Enter number:");
                Node<int> node = new Node<int>(int.Parse(Console.ReadLine()));
                tmp.SetNext(node);
            }
            else if(tav == 'ג')
            {
                while (tmp.GetNext().GetNext() != null)
                {
                    tmp = tmp.GetNext();
                }
                tmp.SetNext(null);
            }
            else if(tav == 'ה')
            {
                while(tmp != null)
                {
                    Console.WriteLine(tmp.GetInfo());
                    tmp = tmp.GetNext();
                }
            }
            else if(tav == 'פ')
            {
                while(tmp != null)
                {
                    tmp.SetInfo(0);
                    tmp = tmp.GetNext();
                }
            }
            return n1;
        }
        public static void Main(string[] args)
        {

            Node<Oil> o5 = new Node<Oil>(new Oil(100));
            Node<Oil> o4 = new Node<Oil>(new Oil(500), o5);
            Node<Oil> o3 = new Node<Oil>(new Oil(50), o4);
            Node<Oil> o2 = new Node<Oil>(new Oil(25), o3);
            Node<Oil> o1 = new Node<Oil>(new Oil(1000), o2);
            Node<Oil> tmp = o1;
            while(tmp != null)
            {
                empty(tmp.GetInfo());
                tmp = tmp.GetNext();
            }
        }
        public static Oil Smallest(Node<Oil> n1)
        {
            Node<Oil> tmp = n1;
            Oil S = tmp.GetInfo();
            tmp = tmp.GetNext();
            while(tmp != null)
            {
                if (tmp.GetInfo().GetQuantity() < S.GetQuantity())
                {
                    S = tmp.GetInfo();
                }
                tmp = tmp.GetNext();
            }
            return S;
        }
        public static void AddToSmallest(Node<Oil> n1, double amount)
        {
            Smallest(n1).AddOil(amount);
        }
        public static Oil empty(Oil o)
        {
            o.Pour(o.GetQuantity());
            return o;
        }
    }
}
