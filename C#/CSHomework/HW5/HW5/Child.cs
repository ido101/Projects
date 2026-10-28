using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HW5
{
    internal class Child
    {
        private string name;
        private string id;
        private char gender;
        private Date birthDate;
        
        public Child(string name, string id, char gender, Date birthDate)
        {
            this.name = name;
            this.id = id;
            this.gender = gender;
            this.birthDate = new Date(birthDate);
        }
        public bool isSameBithday(Child other)
        {
            if(birthDate.Equals(other.birthDate))
            {
                return true;
            }
            return false;
        }
        public string GetName() { return name; }
        public string GetId() { return id; }
        public char GetGender() { return gender;}
        public Date GetBirthDate() { return birthDate;}
        public void SetBirthDate(Date birthDate) { this.birthDate = new Date(birthDate);}
        public void SetGender(char gender) { this.gender = gender;}
        public void SetName(string name) { this.name = name;}
        public void SetId(string id) { this.id = id;}
    }
}
