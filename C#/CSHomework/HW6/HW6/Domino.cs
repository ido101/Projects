using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HW6
{
    internal class Domino
    {
        int num1;
        int num2;
        public Domino(int num1, int num2)
        {
            this.num1 = num1;
            this.num2 = num2;
        }
        public int getNum1() { return num1; }
        public int getNum2() { return num2; }
        public void setNum1(int num1) { this.num1 = num1;} 
        public void setNum2(int num2) { this.num2 = num2; }
        public bool Exist(int num)
        {
            if(num == num1 || num == num2) return true;
            return false;
        }
    }
}
