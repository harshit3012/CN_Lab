<div align='center'>
 <h1> Class / Lab session on RIP routing </h1>
 <h4>06 November 2020</h4>
</div>

# Configuring RIP Routing Protocol in Routers

## Procedure

-   Topology, as shown in image, was created using 3 Router-PTs, and 2 PCs.

-   IP addresses were assigned to Router and the PC as shown in topology.

    ![topo](images/topology.png)

-   Network addresses were added with suitable clock rates to the RIP routing table, as shown below.

    ![rip_config](images/router_configs.png)

## Testing

-   Verifying the routes using _`show ip`_ command.

    ![router_routes](images/router_routes.png)

-   Finally, PC0 and PC1 were pinged to each other to test

    ![pc0_pinging_pc1](images/pc0_pinging_pc1.png)

    ![pc1_pinging_pc0](images/pc1_pinging_pc0.png)
