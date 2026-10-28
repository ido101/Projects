using System;
using Unit4.CollectionsLib;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WorkForQuiz
{
    class Book
    {
        public string name { get; set; }
        public Book(string name)
        {
            this.name = name;
        }
        public override string ToString()
        {
            return $"Book name is {name}";
        }
    }
    internal class Program
    {
        
        public static void Main(string[] args)
        {
            Book b = new Book("Book");
            Console.WriteLine(b.name);
        }
    }
}
