<div align='center'>
 <h1>Lab 5 - 02 November 2020</h1>
</div>

# Configuring DHCP within a LAN

## Procedure

-   Topology, as shown in image, was created using Router-PT, 2960 Switch, Server-PT, and 4 PCs.

-   IP addresses were assigned to Router and the server as shown in image below.

    ![topo](images/1_topo.png)

-   DHCP service in the Server0 was enabled with the following configs.

    ![dhcp_service](images/1_dhcp_service.png)

-   DHCP server in the Server0 automatically assigns the IP addresses to PC0, PC1, PC2, PC3 on enabling the DHCP service.

    ![assigned_ips](images/1_auto_assigned.png)

---

# Demonstration of WEB server and DNS

Initialize HTTP server in the Server0.  
Add a record in the DNS to route _`test.com`_ to _`10.0.0.1`_.

## Procedure

-   Topology, as shown in the image below, was created using Server-PT, 2960 Switch, and a PC.

    ![topo](images/2_topo.png)

-   It was first verified that 10.0.0.1 has a HTTP server running.

    ![http_verification](images/2_http_server_verification.png)

-   Then, an address entry was added for _`test.com`_ in the DNS records as shown below.

    ![dns_service](images/2_dns_service.png)

-   PC0 was setup with the following configs.

    ![PC0_config](images/2_PC0_config.png)

-   The DNS server is tested by going to _`test.com`_ URL from PC0

    ![dns_resolved](images/2_pc0_resolved.png)
