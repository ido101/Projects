using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HW6
{
    internal class Child
    {
        private string name;
        private double height;
        public Child(string name, double height)
        {
            this.name = name;
            this.height = height;
        }
        public string GetName()
        {
            return name;
        }
        public double GetHeight()
        {
            return height;
        }
        public void SetName(string name)
        {
                this.name = name;
        }
        public void SetHeight(double height)
        {
            this.height = height;
        }
    }
}
