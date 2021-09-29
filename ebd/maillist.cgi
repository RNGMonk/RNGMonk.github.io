#!/usr/local/bin/perl

# path to the guestbook file in which the entries are stored
$path_book="list.txt";

###########

# allowed referers
@referers = ('eyeball-design.com','207.106.122.98');

###########

# for security reasons, the form fields are cut off if they exceed a certain length
$cut_email    = 70;

###########

# the separator in the guestbook file, do not change this
$sep_expr = "-%&/-";

################################################
#                    program                   #
################################################

sub CutOff {
	if (length($form{$_[0]})>$_[1]) {$form{$_[0]}=substr($form{$_[0]},0,$_[1]);}
}

sub TameHTML {
	# replace <,> by &lt;,&gt;
	$form{$_[0]}=~s/</&lt/g;
	$form{$_[0]}=~s/>/&gt/g;
}

sub check_referer {
   if (@referers && $ENV{'HTTP_REFERER'}) {
      foreach $referer (@referers) {
         if ($ENV{'HTTP_REFERER'} =~ /$referer/) {
            $ref = 1;
            last;
         }
      }
   }
   else {
      $ref = 1;
   }
   if ($ref != 1) {
	print "Content-type: text/html\n\n";
	print <<endOfHTML;
<html>
<body>
<center>
<h1>BAD REFERER !</h1>
<p>
A page other than annamaria.net tried to call guestbook_sign.pl.<br>
This script will only work when called by an annamaria.net page.
</center>
</body>
</html>
endOfHTML
	exit;
   }
}


# data from form into hash %form
if($ENV{'REQUEST_METHOD'} eq 'GET')
 {
  $Daten = $ENV{'QUERY_STRING'}
 }
else
 {
  read(STDIN, $Daten, $ENV{'CONTENT_LENGTH'});
}
@form_fields = split(/&/, $Daten);
foreach $Feld (@form_fields)  
 {
  ($name, $value) = split(/=/, $Feld);   
  $value =~ tr/+/ /;
  $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
  $value =~ s/<!--(.|\n)*-->//g;      
  $form{$name}=$value;
 }

&check_referer;

# cut off fields if needed

&CutOff('email',$cut_email);

# rough check for valid email address
if (!($form{'email'}=~/.+@.+/)) { $form{'email'}=''; }

# strip sep character
$form{'email'}=~s/$sep_expr//g;

# get date
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
$date = ($mon+1).".".$mday.".".(1900 + $year);

if ($form{'name'} eq "") {$form{'name'}="n/a";}

$line=$date.$sep_expr.$form{'name'}.$sep_expr.$form{'email'}.$sep_expr.$form{'url'}.$sep_expr.$form{'location'}.$sep_expr.$form{'comment'}.$sep_expr.$ENV{'REMOTE_ADDR'}."\n";

############################ WRITE TO FILE #################################################

	open(FILE,">>$path_book") || die "error while opening guestbook file $path_book: $!\n";
	print FILE $form{'email'};
	print FILE "\n";
	close FILE;

#######################################
#        send back html page          #
#######################################

print "Content-type: text/html\n\n";
print <<ReturnPage;

<HTML><head> <TITLE>Eyeball Site</TITLE></HEAD>

<BODY text=white link=c4aF64 vlink=c4aF64 bgcolor=#000000> 
<center>
<br><br><br><br><br>
	<table border=0 cellspacing=0 cellpadding=0 bgcolor=64573c width=272>
	<tr><td><img src=/images/contact/windowtop.gif border=0 width=272 height=9><br></td></tr>
	<tr><td><center>

	<table border=0 cellpadding=10><tr><td>
		<font face=arial color=e4cF84 size=-1><b>
		<center><h3>Your email address has been added to the list</h3>
		<form>
		<input type=button value="Previous page" onclick="history.go(-1)">	
	
	</td></tr></table>
	</td></tr>
	<tr><td><img src=/images/contact/windowbottom.gif border=0 width=272 height=9><br></td></tr>
	</table>

	</form>
	</td></tr></table>

</body></html>


ReturnPage

