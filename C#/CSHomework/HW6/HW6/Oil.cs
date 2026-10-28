using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HW6
{
    internal class Oil
    {
        double capacity;
        double quantity;
        public Oil(double capacity)
        {
            quantity = 0;
            this.capacity = capacity;
        }
        public double GetCapacity()
        {
            return capacity;
        }
        public double GetQuantity()
        {
            return quantity;
        }
        public void SetCapacity(double capacity)
        {
            this.capacity = capacity;
        }
        public void SetQuantity(double quantity)
        {
            this.quantity = quantity;
        }
        public bool AddOil(double quantity)
        {
            if (this.quantity + quantity <= capacity)
            {
                this.quantity += quantity;
                return true;
            }
            return false;
        }
        public double Pour(double quantity)
        {
            if (this.quantity - quantity >= 0)
            {
                this.quantity -= quantity;
            }
            return quantity;
        }
    }
}
