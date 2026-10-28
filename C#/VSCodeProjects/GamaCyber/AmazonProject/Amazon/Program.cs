using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;



internal class Program
{
    public static void Main(string[] args)
    {
        // יצירת מערכת אמזון ראשית
        Amazon amazon = new Amazon();


        // יצירת ספרים עם שם, מחיר, מספר עמודים ונפח
        Books b1 = new Books("Harry Poter", 50.99, 350, 5, Vcup.squardcm);
        Books b2 = new Books("Dod arye", 99.99, 100, 10.9, Vcup.squardcm);
        Books b3 = new Books("a adonit ve a rochel", 30.99, 250, 5, Vcup.squredmeter);


        // יצירת מוצרי לבוש (חולצות ונעליים) עם שם, מחיר, תמונה, מידה ונפח
        Tshirt tshirt = new Tshirt("T1", 39.59, "ssddd", ClothingSize.M, 3, Vcup.squredmeter);
        Shoe jordan = new Shoe("air jordan 1 dior", 5000.99, "11wwd", 44.5, 5, Vcup.squardcm);


        // יצירת חנויות שונות
        Store Tzometsfarim = new Store();
        Store nike = new Store();


        // הוספת מוצרים לחנויות – שימוש בקומפוזיציה: חנות "מחזיקה" מוצרים
        Tzometsfarim.NewProduct(b1);
        Tzometsfarim.NewProduct(b2);
        Tzometsfarim.NewProduct(b3);
        nike.NewProduct(tshirt);
        nike.NewProduct(jordan);


        // יצירת לקוח חדש
        Customer daniel = new Customer("Daniel");
        List<Product> danisal = new List<Product>();
        amazon.AddCustomer(daniel);
        List<Product> danisal2 = new List<Product>();


        // הוספת מוצרים להזמנה של דניאל
        danisal.Add(b1);
        danisal.Add(b2);
        danisal.Add(tshirt);
        danisal.Add(jordan);
        danisal.Add(jordan);


        // יצירת הזמנה עם רשימת מוצרים וכתובת
        // שימוש בקומפוזיציה: הזמנה מכילה כתובת ומשתמשת במחלקת Shipping
        Order order1 = new Order(danisal, new Address(Country.Israel, "Ramat Gan", "rabi shimon", "12"));
        Order order2 = new Order(danisal, new Address(Country.Canada, "Ramat Gan", "rabi shimon", "12"));
        Order order3 = new Order(danisal2, new Address(Country.Israel, "Ramat Gan", "rabi shimon", "12"));


        // הוספת הזמנה ללקוח
        daniel.Addorder(order1);


        // הדפסת מחיר כולל של ההזמנה (כולל עלות משלוח)
        Console.WriteLine(order1.CalculateTotalPrice());


        // הדפסת כל ההזמנות של משתמש עם Id = 1
        foreach (var order in amazon.OrdersByuser(1))
        {
            order.PrintOrder();
        }


        // רשימה עם כמה הזמנות לצורך בדיקה
        List<Order> orderss = new List<Order>();
        orderss.Add(order1);
        orderss.Add(order2);
        orderss.Add(order3);


        // סינון הזמנות לפי מדינה (ישראל)
        foreach (var order in amazon.FOBC(orderss, Country.Israel))
        {
            Console.WriteLine(order.Id);
        }


        // בדיקת הוספת הזמנה לארגז ירוק
        GreenBox greeni = new GreenBox();
        Console.WriteLine(greeni.AddItem(order3));
        greeni.POI(); // הדפסת כל המזהים של ההזמנות בארגז
    }
}


// Enum ליחידות נפח – משמש למדידת "גודל" המוצר
enum Vcup
{
    squredmeter,
    squardcm,
    squardnanometer,
}


// Enum למידות בגדים
enum ClothingSize
{
    XS,
    S,
    M,
    L,
    XL,
    XXL
}


// מחלקת הזמנה
class Order
{
    private static int nextId = 1; // מזהה אוטומטי להזמנות
    private DateTime time; // תאריך ביצוע ההזמנה (לא בשימוש כרגע)
    private IList<Product> products; // המוצרים בהזמנה
    public Address OAddress { get; set; } // כתובת למשלוח – קומפוזיציה: Order "מחזיקה" Address
    Shipping shipping; // עלות משלוח – קומפוזיציה: Order "מחזיקה" Shipping


    public Order(IList<Product> products, Address address)
    {
        Id = nextId++; // כל הזמנה מקבלת מזהה ייחודי
        this.products = products;
        this.OAddress = address;


        // חישוב עלות משלוח לפי נפח כולל של ההזמנה
        this.shipping = new Shipping(CalculateTotalVolume());
    }


    public int Id { get; private set; } // פרופרטי לקריאה בלבד (Id)


    // חישוב המחיר הכולל של המוצרים בלבד (ללא משלוח)
    public double CalculateTotalProductePrice()
    {
        double totalPrice = 0;
        foreach (var product in this.products)
        {
            totalPrice += product.getPrice();
        }
        return totalPrice;
    }


    // חישוב המחיר הכולל של ההזמנה כולל משלוח
    public double CalculateTotalPrice()
    {
        double totalPrice = 0;
        foreach (var product in this.products)
        {
            totalPrice += product.getPrice();
        }
        return totalPrice + shipping.ShipingPrice();
    }


    // חישוב נפח כולל של כל המוצרים בהזמנה
    public double CalculateTotalVolume()
    {
        double totalVolume = 0;
        foreach (var product in this.products)
        {
            totalVolume += product.GetVolume();
        }
        return totalVolume;
    }


    // הדפסת פרטי ההזמנה למסך
    public void PrintOrder()
    {
        Console.WriteLine("____________" + "order number:" + Id + "____________");
        foreach (var product in this.products)
            Console.WriteLine(product.getName() + ":" + product.getPrice());
        Console.WriteLine("total:" + CalculateTotalProductePrice());
        Console.WriteLine("________________________");
    }
}


// מחלקת אב מופשטת (abstract) – מסביר למה לא אינטרפייס:
// 1. יש קוד משותף לכל המוצרים (שם, מחיר, נפח).
// 2. אינטרפייס לא מאפשר קוד מוכן, רק חתימות.
// 3. ירושה מאפשרת שיתוף לוגיקה במקום לשכפל קוד.
abstract class Product
{
    private string name;
    private double price;
    private double volume;
    Vcup vcup;


    public Product(string name, double price, double volume, Vcup vcup)
    {
        this.name = name;
        this.price = price;
        this.volume = volume;
        this.vcup = vcup;
    }


    // מחזיר נפח המוצר לאחר המרה ליחידה אחידה
    public double GetVolume()
    {
        switch (vcup)
        {
            case Vcup.squredmeter:
                return this.volume * 100; // דוגמה להמרה
            case Vcup.squardnanometer:
                return this.volume * 7; // דוגמה אחרת
        }
        return this.volume;
    }


    public string getName() { return this.name; }
    public double getPrice() { return this.price; }
}


// מחלקת אב ללבוש – עדיין abstract כי לא נרצה ליצור Clothing ישירות
abstract class Clothing : Product
{
    private string picture; // קישור לתמונה


    public Clothing(string name, double price, string picture, double volume, Vcup vcup)
        : base(name, price, volume, vcup)
    {
        this.picture = picture;
    }


    public string getPicture() { return this.picture; }
}


// מחלקה לנעליים – ירושה מ-Clothing
class Shoe : Clothing
{
    public double Size { get; set; } // מידה מספרית


    public Shoe(string name, double price, string picture, double size, double volume, Vcup vcup)
        : base(name, price, picture, volume, vcup)
    {
        Size = size;
    }
}


// מחלקה לחולצות – ירושה מ-Clothing
class Tshirt : Clothing
{
    private ClothingSize size; // מידה (Enum)


    public Tshirt(string name, double price, string picture, ClothingSize size, double volume, Vcup vcup)
        : base(name, price, picture, volume, vcup)
    {
        this.size = size;
    }
}


// מחלקת ספרים – ירושה מ-Product
class Books : Product
{
    private int pages; // מספר עמודים


    public Books(string name, double price, int pages, double volume, Vcup vcup)
        : base(name, price, volume, vcup)
    {
        this.pages = pages;
    }
}


// מחלקת לקוח – שומרת הזמנות
class Customer
{
    private static int nextId = 1; // מזהה אוטומטי
    public int Id { get; private set; }
    private string name;
    private IList<Order> orders;


    public Customer(string name)
    {
        Id = nextId++;
        this.name = name;
        orders = new List<Order>(); // קומפוזיציה: לקוח "מחזיק" הזמנות
    }


    public void Addorder(Order order)
    {
        this.orders.Add(order);
    }


    public IList<Order> GetOrders()
    {
        return this.orders;
    }
}


// מחלקת חנות – שומרת מוצרים, לקוחות והזמנות
class Store
{
    private IList<Product> items;
    private IList<Order> orders;
    private IList<Customer> customers;


    public Store()
    {
        this.items = new List<Product>();
        this.orders = new List<Order>();
        this.customers = new List<Customer>();
    }


    // הוספת מוצר לחנות
    public void NewProduct(Product product)
    {
        this.items.Add(product);
    }
}


// מחלקת Amazon – מרכזת חנויות ולקוחות
class Amazon
{
    private IList<Customer> customers;
    private IList<Store> stores;


    public Amazon()
    {
        customers = new List<Customer>();
        stores = new List<Store>();
    }


    public void AddCustomer(Customer customer)
    {
        this.customers.Add(customer);
    }


    public void AddStore(Store store)
    {
        stores.Add(store);
    }


    // החזרת ההזמנות של לקוח לפי Id – שימוש ב-LINQ
    public IList<Order> OrdersByuser(int userid)
    {
        IList<Customer> customer1 = this.customers
                .Where(customer => customer.Id == userid)
                .ToList();


        return customer1[0].GetOrders();
    }


    // סינון הזמנות לפי מדינה
    public IList<Order> FOBC(IList<Order> many, Country country)
    {
        return many.Where(order => order.OAddress.GetCountry() == country).ToList();
    }
}


// מחלקת כתובת – קומפוזיציה עם Order
class Address
{
    private Country country;
    private string city;
    private string streetAddress;
    private string houseNumber;


    public Address(Country country, string city, string streetAddress, string houseNumber)
    {
        this.country = country;
        this.city = city;
        this.streetAddress = streetAddress;
        this.houseNumber = houseNumber;
    }


    public Country GetCountry() { return this.country; }
}


// Enum של מדינות
enum Country
{
    Israel,
    Canada,
    New_York,
    Florida
}


// מחלקת משלוחים – מחשבת עלות משלוח לפי נפח
class Shipping
{
    public double Volume { get; set; }


    public Shipping(double volume)
    {
        Volume = volume;
    }


    // פונקציה שמחזירה את עלות המשלוח
    public double ShipingPrice()
    {
        return Volume; // אפשר לשנות לפי נוסחה אמיתית
    }
}


// צבעי ארגזים
enum Boxcolor
{
    Green,
    Red
}


// מחלקת אב מופשטת לארגזים – כל ארגז מחזיק הזמנות
abstract class Box
{
    private IList<Order> orders;
    private Country country; // כל ארגז יכול להכיל הזמנות רק ממדינה אחת
    public double SpareSpace { get; set; } // מקום פנוי בארגז


    public Box(double sparespace)
    {
        SpareSpace = sparespace;
        orders = new List<Order>();
    }


    // הוספת הזמנה לארגז
    public bool AddItem(Order order)
    {
        double x = order.CalculateTotalVolume();
        if (SpareSpace >= x)
        {
            if (orders.Count == 0)
                country = order.OAddress.GetCountry(); // קובע מדינה לפי ההזמנה הראשונה


            if (country == order.OAddress.GetCountry())
            {
                SpareSpace -= x;
                orders.Add(order);
                return true;
            }
        }
        return false;
    }


    // הדפסת כל מזהי ההזמנות בארגז
    public void POI()
    {
        Console.WriteLine("orders ids in box__________");
        foreach (Order order in orders)
            Console.WriteLine(order.Id);
        Console.WriteLine("__________");
    }
}


// ארגז ירוק – גודל קטן (50)
class GreenBox : Box
{
    public GreenBox() : base(50) { }
}


// ארגז אדום – גודל גדול (200)
class RedBox : Box
{
    public RedBox() : base(200) { }
}