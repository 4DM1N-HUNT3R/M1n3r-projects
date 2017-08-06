#!/bin/bash 
resize -s 36 131 > /dev/null
clear
banner() 
{
echo -e '\e[1;36m' "██╗  ██╗ █████╗ ██╗     ██╗  ██╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗"     
echo -e '\e[1;36m' "██║ ██╔╝██╔══██╗██║     ██║ ██╔╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗"    
echo -e '\e[1;36m' "█████╔╝ ███████║██║     █████╔╝ ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝"    
echo -e '\e[1;36m' "██╔═██╗ ██╔══██║██║     ██╔═██╗ ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗"   
echo -e '\e[1;36m' "██║  ██╗██║  ██║███████╗██║  ██╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║"    
echo -e '\e[1;36m' "╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝"    
}

banner

banner1()
{
echo "██████╗ ██╗███████╗██████╗ ██╗    ██╗██╗ █████╗ ███████╗████████╗██╗  ██╗ ██████╗ ██╗    ██╗ █████╗ ███╗   ██╗██╗███████╗"
echo "██╔══██╗██║██╔════╝██╔══██╗██║    ██║██║██╔══██╗██╔════╝╚══██╔══╝██║ ██╔╝██╔═══██╗██║    ██║██╔══██╗████╗  ██║██║██╔════╝"
echo "██████╔╝██║█████╗  ██████╔╝██║ █╗ ██║██║███████║███████╗   ██║   █████╔╝ ██║   ██║██║ █╗ ██║███████║██╔██╗ ██║██║█████╗"  
echo "██╔═══╝ ██║██╔══╝  ██╔══██╗██║███╗██║██║██╔══██║╚════██║   ██║   ██╔═██╗ ██║   ██║██║███╗██║██╔══██║██║╚██╗██║██║██╔══╝"  
echo "██║     ██║███████╗██║  ██║╚███╔███╔╝██║██║  ██║███████║   ██║   ██║  ██╗╚██████╔╝╚███╔███╔╝██║  ██║██║ ╚████║██║███████╗"
echo "╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝"
}

banner2()
{
echo -e '\e[0;32m' "██████╗  ██████╗ ████████╗███████╗ ██████╗  ██████╗ ██╗    ██╗ █████╗ ███╗   ██╗██╗███████╗"
echo -e '\e[0;32m' "██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝██╔════╝ ██╔═══██╗██║    ██║██╔══██╗████╗  ██║██║██╔════╝"
echo -e '\e[0;32m' "██████╔╝██║   ██║   ██║   █████╗  ██║  ███╗██║   ██║██║ █╗ ██║███████║██╔██╗ ██║██║█████╗  "
echo -e '\e[0;32m' "██╔═══╝ ██║   ██║   ██║   ██╔══╝  ██║   ██║██║   ██║██║███╗██║██╔══██║██║╚██╗██║██║██╔══╝  "
echo -e '\e[0;32m' "██║     ╚██████╔╝   ██║   ███████╗╚██████╔╝╚██████╔╝╚███╔███╔╝██║  ██║██║ ╚████║██║███████╗"
echo -e '\e[0;32m' "╚═╝      ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝"
} 

banner3()
{
echo -e '\e[0;33m' " ██████╗  ██████╗ ██████╗  █████╗ ██╗    ██╗ █████╗ ███╗   ██╗██╗███████╗"
echo -e '\e[0;33m' " ██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██║    ██║██╔══██╗████╗  ██║██║██╔════╝"
echo -e '\e[0;33m' " ██║  ██║██║   ██║██║  ██║███████║██║ █╗ ██║███████║██╔██╗ ██║██║█████╗"  
echo -e '\e[0;33m' " ██║  ██║██║   ██║██║  ██║██╔══██║██║███╗██║██╔══██║██║╚██╗██║██║██╔══╝"  
echo -e '\e[0;33m' " ██████╔╝╚██████╔╝██████╔╝██║  ██║╚███╔███╔╝██║  ██║██║ ╚████║██║███████╗"
echo -e '\e[0;33m' " ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝"  
}				

banner4()
{
echo -e '\e[0;34m' " ██████╗ ██████╗ ███████╗     ██╗███╗   ███╗ ██████╗ ██╗    ██╗ █████╗ ███╗   ██╗██╗███████╗"
echo -e '\e[0;34m' "██╔═══██╗██╔══██╗██╔════╝     ██║████╗ ████║██╔═══██╗██║    ██║██╔══██╗████╗  ██║██║██╔════╝"
echo -e '\e[0;34m' "██║   ██║██║  ██║█████╗       ██║██╔████╔██║██║   ██║██║ █╗ ██║███████║██╔██╗ ██║██║█████╗"  
echo -e '\e[0;34m' "██║   ██║██║  ██║██╔══╝  ██   ██║██║╚██╔╝██║██║   ██║██║███╗██║██╔══██║██║╚██╗██║██║██╔══╝"  
echo -e '\e[0;34m' "╚██████╔╝██████╔╝███████╗╚█████╔╝██║ ╚═╝ ██║╚██████╔╝╚███╔███╔╝██║  ██║██║ ╚████║██║███████╗"
echo -e '\e[0;34m'  "╚═════╝ ╚═════╝ ╚══════╝ ╚════╝ ╚═╝     ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝"
}                                      

banner5()
{ 
echo -e '\e[0;35m' "███╗   ███╗███╗   ██╗ ██████╗ ███████╗███████╗███╗   ██╗██╗███████╗"
echo -e '\e[0;35m' "████╗ ████║████╗  ██║██╔═══██╗╚══███╔╝██╔════╝████╗  ██║██║██╔════╝"
echo -e '\e[0;35m' "██╔████╔██║██╔██╗ ██║██║   ██║  ███╔╝ █████╗  ██╔██╗ ██║██║█████╗"  
echo -e '\e[0;35m' "██║╚██╔╝██║██║╚██╗██║██║   ██║ ███╔╝  ██╔══╝  ██║╚██╗██║██║██╔══╝"  
echo -e '\e[0;35m' "██║ ╚═╝ ██║██║ ╚████║╚██████╔╝███████╗███████╗██║ ╚████║██║███████╗"
echo -e '\e[0;35m' "╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝╚══════╝"
}                                                                  

banner6()
{
echo -e '\e[0;36m' "██████╗ ███████╗██╗███████╗██╗     ███████╗███╗   ██╗██╗███████╗"
echo -e '\e[0;36m' "██╔══██╗╚══███╔╝██║██╔════╝██║     ██╔════╝████╗  ██║██║██╔════╝"
echo -e '\e[0;36m' "██║  ██║  ███╔╝ ██║█████╗  ██║     █████╗  ██╔██╗ ██║██║█████╗"  
echo -e '\e[0;36m' "██║  ██║ ███╔╝  ██║██╔══╝  ██║     ██╔══╝  ██║╚██╗██║██║██╔══╝"  
echo -e '\e[0;36m' "██████╔╝███████╗██║███████╗███████╗███████╗██║ ╚████║██║███████╗"
echo -e '\e[0;36m' "╚═════╝ ╚══════╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝╚══════╝"
}

banner7()
{
echo -e '\e[0;31m' "██████╗  ██████╗ ██╗     ███████╗    ████████╗██████╗  ██████╗      ██╗██╗  ██╗ █████╗ ████████╗ █████╗ "    
echo -e '\e[0;31m' "██╔══██╗██╔═══██╗██║     ██╔════╝    ╚══██╔══╝██╔══██╗██╔═══██╗     ██║██║ ██╔╝██╔══██╗╚══██╔══╝██╔══██╗"    
echo -e '\e[0;31m' "██████╔╝██║   ██║██║     █████╗         ██║   ██████╔╝██║   ██║     ██║█████╔╝ ███████║   ██║   ███████║"    
echo -e '\e[0;31m' "██╔═══╝ ██║   ██║██║     ██╔══╝         ██║   ██╔══██╗██║   ██║██   ██║██╔═██╗ ██╔══██║   ██║   ██╔══██║"    
echo -e '\e[0;31m' "██║     ╚██████╔╝███████╗███████╗       ██║   ██║  ██║╚██████╔╝╚█████╔╝██║  ██╗██║  ██║   ██║   ██║  ██║"    
echo -e '\e[0;31m' "╚═╝      ╚═════╝ ╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝" 
                                          
echo -e '\e[0;31m' "██████╗ ██████╗  ██████╗ ███████╗████████╗ ██████╗ ██╗  ██╗ █████╗ ████████╗███╗   ██╗███████╗ ██████╗  ██████╗" 
echo -e '\e[0;31m' "██╔══██╗██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝██╔═══██╗██║ ██╔╝██╔══██╗╚══██╔══╝████╗  ██║██╔════╝██╔════╝ ██╔═══██╗"
echo -e '\e[0;31m' "██████╔╝██████╔╝██║   ██║███████╗   ██║   ██║   ██║█████╔╝ ███████║   ██║   ██╔██╗ ██║█████╗  ██║  ███╗██║   ██║"
echo -e '\e[0;31m' "██╔═══╝ ██╔══██╗██║   ██║╚════██║   ██║   ██║   ██║██╔═██╗ ██╔══██║   ██║   ██║╚██╗██║██╔══╝  ██║   ██║██║   ██║"
echo -e '\e[0;31m' "██║     ██║  ██║╚██████╔╝███████║   ██║   ╚██████╔╝██║  ██╗██║  ██║   ██║   ██║ ╚████║███████╗╚██████╔╝╚██████╔╝"
echo -e '\e[0;31m' "╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝╚══════╝ ╚═════╝  ╚═════╝"
}

banner8()
{
echo -e '\e[0;30m' "██████╗  ██████╗ ██╗     ███████╗     ██████╗ █████╗ ██╗     ██╗  ██╗ ██████╗ ██╗    ██╗██╗████████╗███████╗"
echo -e '\e[0;30m' "██╔══██╗██╔═══██╗██║     ██╔════╝    ██╔════╝██╔══██╗██║     ██║ ██╔╝██╔═══██╗██║    ██║██║╚══██╔══╝██╔════╝"
echo -e '\e[0;30m' "██████╔╝██║   ██║██║     █████╗      ██║     ███████║██║     █████╔╝ ██║   ██║██║ █╗ ██║██║   ██║   █████╗"  
echo -e '\e[0;30m' "██╔═══╝ ██║   ██║██║     ██╔══╝      ██║     ██╔══██║██║     ██╔═██╗ ██║   ██║██║███╗██║██║   ██║   ██╔══╝"  
echo -e '\e[0;30m' "██║     ╚██████╔╝███████╗███████╗    ╚██████╗██║  ██║███████╗██║  ██╗╚██████╔╝╚███╔███╔╝██║   ██║   ███████╗"
echo -e '\e[0;30m' "╚═╝      ╚═════╝ ╚══════╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═╝   ╚═╝   ╚══════╝" 

echo -e '\e[0;30m' "██╗     ██████╗ ██████╗      ██╗███████╗████████╗ ██████╗ ███████╗ ██████╗    ███████╗████████╗ ██████╗ ███████╗██╗  ██╗ █████╗" 
echo -e '\e[0;30m' "██║    ██╔═══██╗██╔══██╗     ██║██╔════╝╚══██╔══╝██╔═══██╗██╔════╝██╔════╝    ██╔════╝╚══██╔══╝██╔═══██╗╚══███╔╝██║ ██╔╝██╔══██╗"
echo -e '\e[0;30m' "██║    ██║   ██║██████╔╝     ██║█████╗     ██║   ██║   ██║███████╗██║         ███████╗   ██║   ██║   ██║  ███╔╝ █████╔╝ ███████║"
echo -e '\e[0;30m' "██║    ██║   ██║██╔══██╗██   ██║██╔══╝     ██║   ██║   ██║╚════██║██║         ╚════██║   ██║   ██║   ██║ ███╔╝  ██╔═██╗ ██╔══██║"
echo -e '\e[0;30m' "██║    ╚██████╔╝██████╔╝╚█████╔╝███████╗   ██║   ╚██████╔╝███████║╚██████╗    ███████║   ██║   ╚██████╔╝███████╗██║  ██╗██║  ██║"
echo -e '\e[0;30m' "╚═╝     ╚═════╝ ╚═════╝  ╚════╝ ╚══════╝   ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝    ╚══════╝   ╚═╝    ╚═════╝ ╚══════╝╚═      ╚═╝  ╚═╝"  
}

banner9()
{
echo -e '\e[0;33m' "██████╗  ██████╗ ██╗     ███████╗    ████████╗██████╗  █████╗ ██████╗ ███████╗███████╗██╗   ██╗"
echo -e '\e[0;33m' "██╔══██╗██╔═══██╗██║     ██╔════╝    ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══███╔╝██║   ██║"
echo -e '\e[0;33m' "██████╔╝██║   ██║██║     █████╗         ██║   ██████╔╝███████║██████╔╝█████╗    ███╔╝ ██║   ██║"
echo -e '\e[0;33m' "██╔═══╝ ██║   ██║██║     ██╔══╝         ██║   ██╔══██╗██╔══██║██╔═══╝ ██╔══╝   ███╔╝  ██║   ██║"
echo -e '\e[0;33m' "██║     ╚██████╔╝███████╗███████╗       ██║   ██║  ██║██║  ██║██║     ███████╗███████╗╚██████╔╝"
echo -e '\e[0;33m' "╚═╝      ╚═════╝ ╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚══════╝ ╚═════╝ "
}

banner10()
{
echo "██████╗  ██████╗ ██╗     ███████╗     ██████╗ █████╗ ██╗     ██╗  ██╗ ██████╗ ██╗    ██╗██╗████████╗███████╗ "   
echo "██╔══██╗██╔═══██╗██║     ██╔════╝    ██╔════╝██╔══██╗██║     ██║ ██╔╝██╔═══██╗██║    ██║██║╚══██╔══╝██╔════╝"    
echo "██████╔╝██║   ██║██║     █████╗      ██║     ███████║██║     █████╔╝ ██║   ██║██║ █╗ ██║██║   ██║   █████╗ "     
echo "██╔═══╝ ██║   ██║██║     ██╔══╝      ██║     ██╔══██║██║     ██╔═██╗ ██║   ██║██║███╗██║██║   ██║   ██╔══╝"      
echo "██║     ╚██████╔╝███████╗███████╗    ╚██████╗██║  ██║███████╗██║  ██╗╚██████╔╝╚███╔███╔╝██║   ██║   ███████╗"    
echo "╚═╝      ╚═════╝ ╚══════╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═╝   ╚═╝   ╚══════╝" 

echo "██╗     ██████╗ ██████╗      ██╗███████╗████████╗ ██████╗ ███████╗ ██████╗    ██╗    ██╗ █████╗ ██╗      ██████╗ █████╗" 
echo "██║    ██╔═══██╗██╔══██╗     ██║██╔════╝╚══██╔══╝██╔═══██╗██╔════╝██╔════╝    ██║    ██║██╔══██╗██║     ██╔════╝██╔══██╗"
echo "██║    ██║   ██║██████╔╝     ██║█████╗     ██║   ██║   ██║███████╗██║         ██║ █╗ ██║███████║██║     ██║     ███████║"
echo "██║    ██║   ██║██╔══██╗██   ██║██╔══╝     ██║   ██║   ██║╚════██║██║         ██║███╗██║██╔══██║██║     ██║     ██╔══██║"
echo "██║    ╚██████╔╝██████╔╝╚█████╔╝███████╗   ██║   ╚██████╔╝███████║╚██████╗    ╚███╔███╔╝██║  ██║███████╗╚██████╗██║  ██║"
echo "╚═╝     ╚═════╝ ╚═════╝  ╚════╝ ╚══════╝   ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝     ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝"
                                                                                                                                                                                                                                                   
}  

banner11()
{
echo -e '\e[0;34m' "██████╗  ██████╗ ██╗     ███████╗     ██████╗ █████╗ ██╗     ██╗  ██╗ ██████╗ ██╗    ██╗██╗████████╗███████╗"    
echo -e '\e[0;34m' "██╔══██╗██╔═══██╗██║     ██╔════╝    ██╔════╝██╔══██╗██║     ██║ ██╔╝██╔═══██╗██║    ██║██║╚══██╔══╝██╔════╝"    
echo -e '\e[0;34m' "██████╔╝██║   ██║██║     █████╗      ██║     ███████║██║     █████╔╝ ██║   ██║██║ █╗ ██║██║   ██║   █████╗  "    
echo -e '\e[0;34m' "██╔═══╝ ██║   ██║██║     ██╔══╝      ██║     ██╔══██║██║     ██╔═██╗ ██║   ██║██║███╗██║██║   ██║   ██╔══╝  "    
echo -e '\e[0;34m' "██║     ╚██████╔╝███████╗███████╗    ╚██████╗██║  ██║███████╗██║  ██╗╚██████╔╝╚███╔███╔╝██║   ██║   ███████╗"    
echo -e '\e[0;34m' "╚═╝      ╚═════╝ ╚══════╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═╝   ╚═╝   ╚══════╝" 

echo -e '\e[0;34m' "██╗     ██████╗ ██████╗      ██╗███████╗████████╗ ██████╗ ███████╗ ██████╗    ██╗  ██╗██╗   ██╗██╗     ██╗"    
echo -e '\e[0;34m' "██║    ██╔═══██╗██╔══██╗     ██║██╔════╝╚══██╔══╝██╔═══██╗██╔════╝██╔════╝    ██║ ██╔╝██║   ██║██║     ██║"    
echo -e '\e[0;34m' "██║    ██║   ██║██████╔╝     ██║█████╗     ██║   ██║   ██║███████╗██║         █████╔╝ ██║   ██║██║     ██║"    
echo -e '\e[0;34m' "██║    ██║   ██║██╔══██╗██   ██║██╔══╝     ██║   ██║   ██║╚════██║██║         ██╔═██╗ ██║   ██║██║     ██║"    
echo -e '\e[0;34m' "██║    ╚██████╔╝██████╔╝╚█████╔╝███████╗   ██║   ╚██████╔╝███████║╚██████╗    ██║  ██╗╚██████╔╝███████╗██║"    
echo -e '\e[0;34m' "╚═╝     ╚═════╝ ╚═════╝  ╚════╝ ╚══════╝   ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝"    
}  

banner12()   
{
echo " ██████╗ ██████╗ ██╗     ██╗ ██████╗███████╗ █████╗ ███╗   ██╗██╗███████╗    ██████╗ ███████╗██╗  ████████╗██╗   ██╗"
echo "██╔═══██╗██╔══██╗██║     ██║██╔════╝╚══███╔╝██╔══██╗████╗  ██║██║██╔════╝    ██╔══██╗██╔════╝██║  ╚══██╔══╝╚██╗ ██╔╝"
echo "██║   ██║██████╔╝██║     ██║██║       ███╔╝ ███████║██╔██╗ ██║██║█████╗      ██║  ██║█████╗  ██║     ██║    ╚████╔╝" 
echo "██║   ██║██╔══██╗██║     ██║██║      ███╔╝  ██╔══██║██║╚██╗██║██║██╔══╝      ██║  ██║██╔══╝  ██║     ██║     ╚██╔╝" 
echo "╚██████╔╝██████╔╝███████╗██║╚██████╗███████╗██║  ██║██║ ╚████║██║███████╗    ██████╔╝███████╗███████╗██║      ██║"   
echo " ╚═════╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝    ╚═════╝ ╚══════╝╚══════╝╚═╝      ╚═╝"
}   
                                                                                                                                                                                                                                                                                                                                          
sleep 1 
                                                            
#sprawdzenie czy dialog jest zainstalowany
which dialog > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e '\e[0;36m' "[ ✔ ] dialog........................[ zainstalowany]"
else
echo ""
echo -e '\e[0;31m' "[ X ] dialog-> nie zainstalowany]"
echo -e '\e[0;31m' "[ ! ] Ten skrypt wymaga dialog]"
xterm -T "☣ INSTALACJA DIALOG ☣" -geometry 102x34 -e "sudo apt-get install dialog -y"
fi

sleep 1 

#sprawdzenie czy dialog jest zainstalowany
which zenity > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e '\e[0;36m' "[ ✔ ] zenity........................[ zainstalowany]"
else
echo ""
echo -e '\e[0;31m' "[ X ] zenity-> nie zainstalowany]"
echo -e '\e[0;31m' "[ ! ] Ten skrypt wymaga zenity]"
xterm -T "☣ INSTALACJA ZENITY ☣" -geometry 102x34 -e "sudo apt-get install zenity -y"
fi

# sprawdzenie uzytkownika obecnie w systemie
if [ $(id -u) != "0" ]; then

      echo -e '\e[0;36m' [!]::[Sprawdzanie zaleznosci] ;
     
      echo -e '\e[0;36m' [✔]::[Sprawdzanie uzytkownika]: $USER ;
      
      echo -e '\e[0;31m' [x]::[not root]: Musisz byc [rootem] by moc wykonac ten skrypt.;
      echo ""
      exit
   	 


else

   echo -e '\e[0;36m' [!]::[Sprawdzanie zaleznosci]: ;
   sleep 1
   echo -e '\e[0;36m' [✔]::[Sprawdzanie uzytkownika]:[+] $USER [+];

fi

while true 
do 
 sleep 0.1
 opcja="++++++++++++++++++WYBIERZ OPCJE+++++++++++++++++++++++++++++++++++"
    opcjalength=${#opcja}                    
    i=0      
    while ((i < 100)); do
        n=$((i*opcjalength / 100))
        printf "\e[00;32m\r%-${opcjalength}s\e[00m" "${opcja:0:n}"
        ((i += RANDOM%5+2))
        sleep 0.03
    done
 echo -e '\n' '\t' '\t' '\e[3m' "-1 - PIERWIASTKOWANIE			     +"
 sleep 0.03
 echo -e  '\t' '\t' '\e[0;32m' "0 - POTEGOWANIE                            +"
 sleep 0.03                                                                   
 echo -e '\t' '\t' '\e[1;33m' "1 - DODAWANIE                              +"
 sleep 0.03
 echo -e '\t' '\t' '\e[1;34m' "2 - ODEJMOWANIE                            +" 
 sleep 0.03
 echo -e '\t' '\t' '\e[1;35m' "3 - MNOZENIE                               +"
 sleep 0.03
 echo -e '\t' '\t' '\e[1;36m' "4 - DZIELENIE                              +"
 sleep 0.03
 echo -e '\t' '\t' '\e[1;31m' "5 - POLE TROJKATA PROSTOKATNEGO            +" 
 sleep 0.03
 echo -e '\t' '\t' '\e[1;30m' "6 - POLE CALKOWITE I OBJETOSC STOZKA       +"
 sleep 0.03
 echo -e '\t' '\t' '\e[0;33m' "7 - POLE TRAPEZU                           +"
 sleep 0.03
 echo -e '\t' '\t' '\e[0;36m' "8 - POLE CALKOWITE I OBJETOSC WALCA        +"
 sleep 0.03
 echo -e '\t' '\t' '\e[0;34m' "9 - POLE CALKOWITE I OBJETOSC KULI         +"
 sleep 0.03
 echo -e '\t' '\t' '\e[0;35m' "10 - OBLICZANIE DELTY			     +"
 sleep 0.03
 echo  -e '\t' '\t' '\e[0;30m' "11 - POLE TROJKATA ROWNOBOCZNEGO           +"
 sleep 0.03
 echo -e '\t' '\t' '\e[1;32m' "12 - WYJSCIE                               +"
 sleep 0.03
 Opcja="+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    Opcjalength=${#Opcja}
    i=0
    while ((i < 100)); do
        n=$((i*Opcjalength / 100))
        printf "\e[00;32m\r%-${Opcjalength}s\e[00m" "${Opcja:0:n}"
        ((i += RANDOM%5+2))
        sleep 0.03
    done 
 sleep 0.03
 echo -n -e '\n' '\e[4;31m' "Kalkulator>"
 read opcje

   #Ladna linia ktora sie pojawi po wybraniu opcji. 
   bar="+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    barlength=${#bar}
    i=0
    while ((i < 100)); do
        n=$((i*barlength / 100))
        printf "\e[00;32m\r%-${barlength}s\e[00m" "${bar:0:n}"
        ((i += RANDOM%5+2))
        sleep 0.03
    done

  #Sprawdzenie czy uzytkownik wpisal liczbe 12 ktora wychodzi ze skryptu
  if [ "$opcje" -eq 12 ]; then 
	sudo dialog --infobox "Wychodzenie........." 10 20
	sleep 3
	clear
	exit
  fi

  #Sprawdzenie czy uzytkownik wpisal liczbe mniejsza niz 12 a jesli to zrobi to wychodzi ze skryptu  
  if [ "$opcje" -lt 13 ]; then 
	sudo zenity --info --text "[+] Opcja istnieje.Mozesz przejsc dalej[+]"  
	sleep 2
	clear
  else
	sudo zenity --error --text "[!] Dostep zabroniony.Opcja nie istnieje Lub wpisano duze lub male litery [!]"
	sleep 2
	clear
	banner
  fi

  case $opcje in 
    -1) banner1
	 sudo python pierwiastek.py
	 sleep 4 
	 clear 
	 banner
	 ;;
    0) banner2
         echo -e '\e[0;34m' "Podaj liczbe do spotegowania"
	 read liczba
	 L=$((liczba * liczba))
	 if [ "$liczba" -eq 0 ]; then 
		echo "Musisz podac liczbe bo zostawiles puste pole lub wpisales zero"
	 else 
	 	echo "WYNIK POTEGOWANIA TO L=$L"
	 	sleep 4
	 	clear
	 	banner
	 fi
	 ;;
    1) banner3
  	 echo -e '\e[1;33m' "Podaj pierwsza liczbe a"
	 read a
	 echo -e '\e[1;33m' "Podaj druga liczba b"
	 read b
	 L=$((a + b))
	 if [[ "$a" -eq 0 && "$b" -eq 0 ]] ; then 
		echo "Musisz podac liczbe bo zostawiles puste pole lub wpisales zero"
	 else
	 	echo "WYNIK DODAWANIA TO L=$L"
	 	sleep 4
	 	clear
	 	banner
	 fi
	 ;;
    2) banner4
         echo -e '\e[1;34m' "Podaj pierwsza liczbe a" 
	 read a
	 echo -e '\e[1;34m' "Podaj druga liczba b"
	 read b
	 L=$((a - b))
	 if [[ "$a" -eq 0 && "$b" -eq 0 ]] ; then 
		echo "Musisz podac liczbe bo zostawiles puste pole lub wpisales zero"
	 else
	 	echo "WYNIK ODEJMOWANIA TO L=$L"
	 	sleep 4
	 	clear
	 	banner
	 fi
	 ;;
    3) banner5
	 echo -e '\e[1;35m' "Podaj pierwsza liczbe a" 
	 read a
	 echo -e '\e[1;35m' "Podaj druga liczba b"
	 read b
	 L=$((a * b))
	 if [[ "$a" -eq 0 && "$b" -eq 0 ]] ; then 
		echo "Musisz podac liczbe bo zostawiles puste pole lub wpisales zero"
	 else
	 	echo "WYNIK MNOZENIA TO L=$L"
	 	sleep 4
	 	clear
	 	banner
	 fi
	 ;;
    4) banner6
        echo -e '\e[1;36m' "Podaj pierwsza liczbe a" 
        read a
        echo -e '\e[1;36m' "Podaj druga liczba b"
        read b
        L=$((a / b))
	if [[ "$a" -eq 0 && "$b" -eq 0 ]] ; then 
		echo "Musisz podac liczbe bo zostawiles puste pole lub wpisales zero"
	else
        	echo "WYNIK DZIELENIA TO L=$L"
		sleep 4
 		clear
		banner
	fi
	;;
    5) banner7
        echo -e '\e[1;31m' "Podaj pierwszy bok a" 
        read a
        echo -e '\e[1;31m' "Podaj drugi bok b"
        read b
        L=$((a * b / 2))
	if [[ "$a" -eq 0 && "$b" -eq 0 ]] ; then 
		echo "Musisz podac liczbe bo zostawiles puste pole lub wpisales zero"
	else
        	echo "POLE TROJKATA PROSTOKOTNEGO TO L=$L"
		sleep 4
		clear
		banner
	fi
	;;
    6) banner8
        echo -e '\e[1;30m' "Podaj TWORZACA" 
        read l
        echo -e '\e[1;30m' "Podaj PROMIEN"
        read r
        echo "Podaj wysokosc"
        read h
	echo $l $r $h
        Pi=3,14
	Pp=$(($Pi * r * r))
	Pb=$(($Pi * r * l))
	Pc=$(($Pi * r * r + l))
        V=$(($Pi * r * r * h / 3))
	if [[ "$l" -eq 0 && "$r" -eq 0 && "$h" -eq 0 ]] ; then 
		echo "Musisz podac liczbe bo zostawiles puste pole lub wpisales zero"
	else
		echo "POLE PODSTAWY STOZKA TO Pp=$Pp"
		echo "POLE BOCZNE STOZKA TO Pb=$Pb"
		echo "POLE CALKOWITE STOZKA TO Pc=$Pc"
		echo "OBJETOSC STOZKA TO V=$V"
		sleep 4
		clear
		banner
	fi
	;;
    7) banner9
	echo -e '\e[3m' "PODAJ DLUGOSC KROTSZEGO BOKU A"
	read A 
	echo -e '\e[3m' "PODAJ DLUGOSC DLUZSZEGO BOKU B"
	read B 
	echo -e '\e[3m' "PODAJ WYSOKOSC H"
	read H
	echo $A $B $H 
	P=$((A + B * H / 2))
	if [[ "$A" -eq 0 && "$B" -eq 0 && "$H" -eq 0 ]] ; then 
		echo "Musisz podac liczbe bo zostawiles puste pole lub wpisales zero"
	else
		echo "POLE TRAPEZU WYNOSI P=$P"
		sleep 4
		clear
		banner
	fi
	;;
    8) banner10
        echo -e '\e[1;30m' "Podaj TWORZACA" 
        read l
        echo -e '\e[1;30m' "Podaj PROMIEN"
        read r
        echo "Podaj wysokosc"
        read h
	echo $l $r $h
        Pi=3,14
	Pp=$(($Pi * r * r))
	Pb=$(($Pi * $Pi * r * h))
	Pc=$(($Pi * $Pi * r * r + h))
        V=$(($Pi * r * r * h))
	if [[ "$l" -eq 0 && "$r" -eq 0 && "$h" -eq 0 ]] ; then 
		echo "Musisz podac liczbe bo zostawiles puste pole lub wpisales zero"
	else
		echo "POLE PODSTAWY WALCA TO Pp=$Pp"
		echo "POLE BOCZNE WALCA TO Pb=$Pb"
		echo "POLE CALKOWITE WALCA TO Pc=$Pc"
		echo "OBJETOSC WALCA TO V=$V"
		sleep 4
		clear
		banner
	fi
	;;
    9) banner11
	echo -e '\e[0;34m' "Podaj PROMIEN"
        read r
	Pc=$((4 * r * r))
	V=$((4 / 3 * r * r * r))
	if [ "$r" -eq 0 ] ; then 
		echo "Musisz podac liczbe bo zostawiles puste pole lub wpisales zero"
	else	
		echo $r
		echo "POLE CALKOWITE KULI WYNOSI Pc=$Pc cm"
		echo "OBJETOSC KULI WYNOSI V=$V cm"
		sleep 4 
		clear 
		banner
	fi
	;; 
    10)banner12
	echo -e '\e[0;35m' "Podaj liczbe a"
	read a
	echo -e '\e[0;35m' "Podaj liczbe b"
	read b 
	echo -e '\e[0;35m' "Podaj liczbe c"
	read c
	echo "Wzor na delte to (b * b - 4 * a * c)"
	if [[ "$a" -eq 0 && "$b" -eq 0 && "$c" -eq 0 ]]; then 
		echo "Musisz podac liczbe bo zostawiles puste pole lub wpisales zero"
	else
		echo a = $a b = $b c = $c
		Delta=$((4 * a * c - b * b))	
		echo "Delta wynosi $Delta"
		sleep 4
		clear
		banner
	fi
	;;
   11) sudo python Pole.py
        sleep 4 
	clear 
	banner
	;; 
   12) exit
esac
done
