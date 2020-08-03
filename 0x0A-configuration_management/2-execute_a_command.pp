# Create a manifest that kills a process named killmenow
exec { 'killmenow':
  command => XS'pkill -f killmenow'
}
