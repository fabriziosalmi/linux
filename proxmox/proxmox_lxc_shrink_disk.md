To reduce the disk size of an LXC container from 128GB to 64GB using bash and the Proxmox hypervisor, you can follow these steps:

1. Connect to the Proxmox host server using SSH or a terminal.
2. Identify the LXC container that you want to resize by running the following command:
   ```
   pct list
   ```
   This command will list all the containers along with their respective IDs.
3. Stop the LXC container that you want to resize by executing the following command:
   ```
   pct stop <container_id>
   ```
   Replace `<container_id>` with the actual ID of your LXC container.
4. Resize the container's disk image using the `resize2fs` command. Assuming the disk is using the `ext4` file system, run the following command:
   ```
   qemu-img resize /var/lib/vz/images/<container_id>/rootfs.img 64G
   ```
   Replace `<container_id>` with the actual ID of your LXC container.
5. Start the container using the following command:
   ```
   pct start <container_id>
   ```
6. Connect to the container using SSH or a terminal.
7. Resize the file system inside the container to match the new disk size by running the following command:
   ```
   resize2fs /dev/sda1 64G
   ```
   Adjust the device name (`/dev/sda1`) if your configuration differs.
8. Verify that the disk size has been reduced by running the following command inside the container:
   ```
   df -h
   ```
   This command will display the current disk usage and sizes.
9. Exit the container.
10. On the Proxmox host server, stop the container again using the following command:
    ```
    pct stop <container_id>
    ```
11. Shrink the disk image to reclaim the unused space by executing the following command:
    ```
    qemu-img resize /var/lib/vz/images/<container_id>/rootfs.img 64G
    ```
12. Start the container using the command:
    ```
    pct start <container_id>
    ```
13. Verify that the disk size has been successfully reduced.

Please note that these instructions assume that the LXC container uses a single partition for the file system. If your setup differs, you may need to adapt the commands accordingly. It's always a good idea to have a backup of your data before performing any disk operations.
