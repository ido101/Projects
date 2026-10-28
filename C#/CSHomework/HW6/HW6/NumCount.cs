using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HW6
{
    internal class NumCount
    {
        int num;
        int count;
        public NumCount(int num, int count)
        {
            this.num = num;
            this.count = count;
        }
        public int getNum()
        {
            return num;
        }
        public int getCount()
        {
            return count;
        }
        public void setNum(int num)
        {
            this.num = num;
        }
        public void setCount(int count)
        {
            this.count = count;
        }
    }
}
