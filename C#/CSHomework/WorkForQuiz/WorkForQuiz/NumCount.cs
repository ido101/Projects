using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WorkForQuiz
{
    internal class NumCount
    {
        private int num;
        private int count;
        public NumCount(int num, int count)
        {
            this.num = num;
            this.count = count;
        }

        public int GetNum()
        {
            return num;
        }
        public int GetCount()
        {
            return count;
        }
        public void SetNum(int num)
        {
            this.num = num;
        }
        public void SetCount(int count)
        {
            this.count = count;
        }
    }
}
