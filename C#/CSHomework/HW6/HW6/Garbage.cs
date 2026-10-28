using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HW6
{
    internal class Garbage
    {
        private string num;
        private double capacity;
        private double quantity;
        private string neighborhood;
        public string GetNum()
        {
            return num;
        }
        public double GetCapacity()
        {
            return capacity;
        }
        public double GetQuantity()
        {
            return quantity;
        }
        public string GetNeighborhood()
        {
            return neighborhood;
        }
        public void SetNum(string num)
        {
            this.num = num;
        
        }
        public void SetCapacity(double capacity)
        {
            this.capacity = capacity;
        }
        public void SetQuantity(double quantity)
        {
            this.quantity = quantity;
        }
        public void SetNeighborood(string neighborhood)
        {
            this.neighborhood = neighborhood;
        }
    }
}
