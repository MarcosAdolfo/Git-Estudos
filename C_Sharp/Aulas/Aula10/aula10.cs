using System; 

namespace Aula10
{

    class aula10
    {
        enum DiasSemanas{dom,seg,ter,qua,qui,sex,sab};
        static void Main(string[] args)
        {
            DiasSemanas ds = DiasSemanas.dom;
            DiasSemanas ds1 = (DiasSemanas)5;
            int ds2 = (int)DiasSemanas.ter;

            Console.WriteLine("{0}\n{1}\n{2}",ds,ds1,ds2);
        }
    }

}
