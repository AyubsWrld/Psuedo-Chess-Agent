#! /usr/bin/perl
use FileHandle;
use IPC::Open2;

if($#ARGV!=1)
{
  print "USAGE: td.pl blackplayer whiteplayer\n"; 
}
else
{

  system("rm -f .newgame.txt");
  system("rm -f .history.txt");

  $aaa = "echo \"BXBXBXBXB\nXBXBXBXBX\">>.newgame.txt";
  system($aaa);
  system($aaa);

  $aaa = "echo \"WXWXOXBXB\">>.newgame.txt";
  system($aaa);
  $aaa = "echo \"XWXWXWXWX\nWXWXWXWXW\">>.newgame.txt";
  system($aaa);
  system($aaa);
  $stop=1;
  $bbb="./".$ARGV[0] . " .newgame.txt B>.B";
  $www="./".$ARGV[1] . " .newgame.txt W>.W";
  open(HH, '>', ".history.txt");

  while($stop!=0)
  {
    system($bbb);
    open(FH, '<', ".B");
    $ll = <FH>;
    close(FH);
    $bl="B:". $ll;
    print $bl;
    print HH $bl;
    $aaa = "./tmovecheck .newgame.txt B " . $ll;
    system($aaa);

    if($?!=0) {close(HH);exit()};

    system($www);
    open(FH, '<', ".W");
    $ll=<FH>;
    close(FH);
    $wl="W:". $ll;
    print$wl;
    print HH $wl;
    $aaa = "./tmovecheck .newgame.txt W " . $ll;
    system($aaa); 

    if($?!=0) {close(HH);exit()};
  }    
#system("rm -f .newgame.txt"); 
}
