using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassHW3
{
    internal class Die
    {
        private string caption;
        private int num;

        public Die(string caption,int num)
        {
            this.caption = caption;
            this.num = num;
        } 
        public Die(string caption)
        {
            this.caption = caption; 
            Random rnd = new Random();
            num = rnd.Next(1, 7);
        }
        public Die(Die other)
        {
            this.num = other.num;
            this.caption = other.caption;
        }
        public override string ToString()
        {
            return "Caption: " + caption + ", Num: " + num;
        }
        public void Roll()
        {
            Random rnd = new Random();
            num = rnd.Next(1, 7);
        }
    }
}
