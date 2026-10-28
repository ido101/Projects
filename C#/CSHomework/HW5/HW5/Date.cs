using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HW5
{
    internal class Date
    {
        private int day;
        private int month;
        private int year;

        public Date(int day, int month, int year)
        {
            this.day = day;
            this.month = month;
            this.year = year;
        }
        public Date(Date date)
        {
            this.day = date.day;
            this.month = date.month;
            this.year = date.year;
        }
        public bool Equals(Date other)
        {
            if(day == other.day && month == other.month&& year == other.year) return true;
            return false;
        }
        public override string ToString()
        {
            return day + "/" + month + "/" + year;
        }
        public int GetDay()
        {
            return day;
        }
        public int GetMonth()
        {
            return month;
        }
        public int GetYear()
        {
            return year;
        }
        public void SetDay(int day)
        {
            this.day = day;
        }
        public void SetMonth(int month)
        {
            this.month = month;
        }
        public void SetYear(int year)
        {
            this.year = year;
        }
    }
}
