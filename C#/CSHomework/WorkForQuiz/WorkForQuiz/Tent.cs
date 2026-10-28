using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WorkForQuiz
{
    internal class Tent
    {
        int capacity;
        string gender;
        int mosquitos;
        public Tent(int capacity, string gender, int mosquitos)
        {
            this.capacity = capacity;
            this.gender = gender;
            this.mosquitos = mosquitos;
        }
        public int getCapacity() { return capacity; }
        public string getGender() { return gender; }
        public int getMosquitos() {  return mosquitos; }
        public void setCapacity(int capacity) { this.capacity = capacity; }
        public void setGender(string gender) { this.gender = gender; }
        public void setMosquitos(int mosquitos) {  this.mosquitos = mosquitos;}
    }
}
