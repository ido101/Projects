enum MaritalStatus
{
    Single,
    Divorced,
    Married
}
abstract class SocialPlatform
{
    #region Properties

    protected IList<User> Users;
    protected IList<Post> Posts;
    protected IList<Chat> groupChats;

    #endregion

    #region Methods

    public SocialPlatform()
    {
        Users = new List<User>();
        Posts = new List<Post>();
        groupChats = new List<Chat>();
    }

    public void AddUser(User user)
    {
        foreach(User existingUser in Users)
        {
            if(user.Equals(existingUser))
            {
                Console.WriteLine("User already exists");
                return;
            }
        }
        Users.Add(user);
    }

    public void AddUser(string firstName, string lastName, int age, MaritalStatus status)
    {
        User user = new User(firstName, lastName, age);
        AddUser(user);
    }

    public void AddPost(Post post)
    {
        foreach(Post existingPost in Posts)
        {
            if(post.Equals(existingPost))
            {
                Console.WriteLine("You have already uploaded this post");
                return;
            }
        }
        Posts.Add(post);
    }

    public void AddPost(User owner, string content)
    {
        Post post = new Post(owner, content);
        AddPost(post);
    }
    
    public void AddPost(User owner, string content, string link)
    {
        Post post = new Post(owner, content, link);
        AddPost(post);
    }
        
    public void SendFriendRequest(SocialMediaUser from, SocialMediaUser to, string message)
    {
        FriendRequest friendRequest = new FriendRequest(from, to, message);
        to.NewFriendRequest(friendRequest);
    }
    
    public Chat CreatGroup(SocialMediaUser user1, SocialMediaUser user2)
    {
        Chat groupChat = new Chat(new List<SocialMediaUser>{user1, user2});
        groupChats.Add(groupChat);
        return groupChat;
    }

    public IList<Chat> AllGroupChatsWith(SocialMediaUser user)
    {
        return groupChats.Where(group => group.IsIn(user)).ToList();
    }
    
    public IList<Message> AllGroupMessagesFrom(SocialMediaUser user)
    {
        return AllGroupChatsWith(user).SelectMany(chat => chat.GetMessages()).ToList().Where(message => message.GetSender().id == user.id).ToList();
    }

    public virtual IList<Post> GetFeed(SocialMediaUser user)
    {
        return this.SortFeed(this.Posts);
    }

    public abstract IList<Post> SortFeed(IList<Post> feed);

    #endregion
}
class Facebook : SocialPlatform
{
    #region Properties

    #endregion
    
    #region Methods
    
    public Facebook() : base() {}
    
    public override IList<Post> GetFeed(SocialMediaUser user)
    {
        IList<Post> feed = new List<Post>();
        foreach(var post in this.Posts)
        {
            User postOwner = post.GetOwner();
            if (user.IsFriend(postOwner))
            {
                feed.Add(post);
            }
        }
        return this.SortFeed(feed);
    }

    public override IList<Post> SortFeed(IList<Post> feed)
    {
        feed = feed.OrderBy(post => post.GetLink() != "").ToList();
        return feed;
    }

    #endregion
}
class Instagram : SocialPlatform
{
    #region Properties

    #endregion
    
    #region Methods
    
    public Instagram() : base() {}
    
    public override IList<Post> SortFeed(IList<Post> feed)
    {
        IList<Post> firstPart = feed.Where(post => post.GetLink() == "").ToList();
        IList<Post> secondPart = feed.Where(post => post.GetLink() != "").ToList();
        firstPart = SortByEngagement(firstPart);
        secondPart = SortByEngagement(secondPart);
        return firstPart.Concat(secondPart).ToList();
    }
    
    private IList<Post> SortByEngagement(IList<Post> feed)
    {
        return feed.OrderBy(post => (post.GetLikes().Count + post.GetComments().Count)).ToList();
    }


    #endregion
}
class User
{
    #region Properties

    private static int nextId = 1;
    protected string firstName;
    protected string lastName;
    protected int age;
    public int id{ get; private set; }

    #endregion
    
    #region Methods

    public User(string firstName, string lastName, int age)
    {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.id = nextId++;
    }

    public override string ToString()
    {
        return $"{this.firstName} {this.lastName}";
    }

    public override bool Equals(object? obj)
    {
        if (obj is User user)
        {
            return this.id == user.id;
        }
        return false;
    }

    public override int GetHashCode()
    {
        return this.id.GetHashCode();
    }

    #endregion
}
class Post
{
    #region Properties

    private static int nextId = 1;
    private User owner;
    private string content;
    private string link;
    private IList<Like> likes;
    private IList<Comment> comments;
    private int id;

    #endregion
    
    #region Methods
    
    public Post(User owner, string content)
    {
        this.owner = owner;
        this.content = content;
        this.link = "";
        this.likes = new List<Like>();
        this.comments = new List<Comment>();
        this.id = nextId++;
    }

    public Post(User owner, string content, string link)
    {
        this.owner = owner;
        this.content = content;
        this.link = link;
        this.likes = new List<Like>();
        this.comments = new List<Comment>();
        this.id = nextId++;
    }

    public string GetLink()
    {
        return link;
    }

    public IList<Like> GetLikes()
    {
        return likes;
    }

    public IList<Comment> GetComments()
    {
        return comments;
    }

    public void AddComment(Comment comment)
    {
        foreach(Comment existingComment in this.comments)
        {
            if(comment == existingComment)
            {
                Console.WriteLine("You have already made this comment.");
                return;
            }
        }
        this.comments.Add(comment);
    }
    
    public void AddLike(Like like)
    {
        foreach(Like existingLike in this.likes)
        {
            if(like.GetOwner().Equals(existingLike.GetOwner()))
            {
                Console.WriteLine("You have already liked this post");
                return;
            }
        }
        this.likes.Add(like);
    }

    public User GetOwner()
    {
        return owner;
    }

    public override string ToString()
    {
        string commentsText = "-------------------------\n";
        foreach(var comment in this.comments)
        {
            commentsText += $"{comment.GetOwner()}\n{comment.GetContent()}\n-------------------------\n";
        }
        return $"Post Owner: {this.owner}\nPost Content: {this.content}\nLike Amount: {this.likes.Count}\nComments:\n{commentsText}";
    }

    public override bool Equals(object? obj)
    {
        if (obj is Post user)
        {
            return this.id == user.id;
        }
        return false;
    }

    public override int GetHashCode()
    {
        return this.id.GetHashCode();
    }

    #endregion
}
class Like
{
    #region Fields

    private User owner;

    #endregion

    #region Methods

    public Like(User owner)
    {
        this.owner = owner;
    }

    public User GetOwner()
    {
        return owner;
    }

    #endregion
}
class Comment
{
    #region Fields

    private User owner;
    private string content;

    #endregion

    #region Methods

    public Comment(User owner, string content)
    {
        this.owner = owner;
        this.content = content;
    }

    public User GetOwner()
    {
        return owner;
    }

    public string GetContent()
    {
        return content;
    }

    #endregion
}
//stage 2
enum RequestStatus
{
    Approved,
    Waiting,
    Rejected
}
class SocialMediaUser : User
{
    #region Fields

    private IList<Connection> friends;
    private MaritalStatus status;
    private IList<FriendRequest> friendRequestsReceived;
    private IList<Chat> chats;

    #endregion

    #region Methods

    public SocialMediaUser(string firstName, string lastName, int age, MaritalStatus status) : base(firstName, lastName, age)
    {
        this.status = status;
        friends = new List<Connection>();
        friendRequestsReceived = new List<FriendRequest>();
        chats = new List<Chat>();
    }

    public IList<FriendRequest> GetFriendRequests()
    {
        return friendRequestsReceived;
    }

    public IList<Chat> GetChats()
    {
        return chats;
    }

    public void NewFriendRequest(FriendRequest friendRequest)
    {
        friendRequestsReceived.Add(friendRequest);
    }

    public void NewFriend(Connection friend)
    {
        friends.Add(friend);
    }
    
    public void ViewFriendRequests()
    {
        foreach(FriendRequest request in friendRequestsReceived)
        {
            Console.WriteLine(request);
        }
    }

    public bool IsFriend(User user)
    {
        //Long way
        // foreach(var friend in friends)
        // {
        //     if(user.GetId() == friend.GetId())
        //     {
        //         return true;
        //     }
        // }
        // return false;

        return friends.Any(connection => connection.GetUser().id == user.id);
    }

    #endregion
}
class FriendRequest
{
    #region Fields

    private SocialMediaUser from;
    private SocialMediaUser to;
    private RequestStatus requestStatus;
    private string message;

    #endregion

    #region Method

    public FriendRequest(SocialMediaUser from, SocialMediaUser to, string message)
    {
        this.from = from;
        this.to = to;
        this.requestStatus = RequestStatus.Waiting;
        this.message = message;
    }

    public void Action(RequestStatus action)
    {
        requestStatus = action;
        if(action == RequestStatus.Approved)
        {
            this.to.NewFriend(new Connection(this.from));
            this.from.NewFriend(new Connection(this.to));
        }
    }


    public override string ToString()
    {
        return $"Friend request from: {this.from}, who says: {this.message}. Request status: {this.requestStatus}.";
    }

    #endregion
}
//stage 4
class Message
{
    private SocialMediaUser from;
    private string content;
    private DateTime messageDate;

    public Message(SocialMediaUser from, string content, DateTime messageDate)
    {
        this.from = from;
        this.content = content;
        this.messageDate = messageDate;
    }

    public SocialMediaUser GetSender()
    {
        return from;
    }
}
class Chat
{
    private IList<SocialMediaUser> users;
    private IList<Message> messages;

    public Chat(IList<SocialMediaUser> users)
    {
        this.users = users;
        messages = new List<Message>();
    }

    public void NewMessage(Message message)
    {
        this.messages.Add(message);
    }

    public IList<Message> GetMessages()
    {
        return this.messages;
    }

    public IList<SocialMediaUser> GetUsers()
    {
        return users;
    }

    public bool IsIn(SocialMediaUser member)
    {
        return this.users.Any(user => user.id == member.id);
    }

    public void AddMember(SocialMediaUser member)
    {
        if(!IsIn(member))
            users.Add(member);
    }
}
class Connection
{
    private SocialMediaUser user;
    private Chat chat;

    public Connection(SocialMediaUser user)
    {
        this.user = user;
        this.chat = new Chat(new List<SocialMediaUser>{user});
    }

    public SocialMediaUser GetUser()
    {
        return user;
    }
}