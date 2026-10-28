using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WorkForQuiz
{
    internal class Person
    {
        string name;
        int time;
        public Person(string name, int time)
        {
            this.name = name;
            this.time = time;
        }
        public int GetTime()
        {
            return time;
        }
    }
}
