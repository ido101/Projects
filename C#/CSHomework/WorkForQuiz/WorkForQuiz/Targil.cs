using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WorkForQuiz
{
    internal class Targil
    {
        string subject;
        int page;
        int questNum;
        public Targil(string subject, int page, int questNum)
        {
            this.subject = subject;
            this.page = page;
            this.questNum = questNum;
        }
    }
}
