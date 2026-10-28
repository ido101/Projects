using System;
using Unit4.CollectionsLib;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WorkForQuiz
{
    internal class OrederedList
    {
        private Node<NumCount> Ist;
        public void InsertNum(int x)
        {
            Node<NumCount> tmp = Ist;
            while (tmp != null)
            {
                if (tmp.GetInfo().GetNum() == x)
                {
                    tmp.GetInfo().SetCount(tmp.GetInfo().GetCount() + 1);
                }
                else if (tmp.GetNext().GetInfo().GetNum() > x&&tmp.GetInfo().GetNum() < x)
                {
                    Node<NumCount> N = new Node<NumCount>(new NumCount(x, 1), tmp.GetNext());
                    tmp.SetNext(N);
                }
                tmp = tmp.GetNext();
            }
        }
        public int ValueN(int n)
        {
            Node<NumCount> tmp = Ist;
            int c = 0;
            while(tmp != null)
            {
                c += tmp.GetInfo().GetCount();
                if(c >= n)
                {
                    return tmp.GetInfo().GetNum();
                }
                tmp = tmp.GetNext();
            }
            return 0;
        }
    }
}
